#!/usr/bin/env node

/**
 * Screenshot Capture Script for UX Audit
 *
 * Usage:
 *   node capture.js <base-url> <output-dir> [--routes route1,route2,...] [--cookies cookie-file.json] [--password pwd] [--width 1280]
 *
 * Examples:
 *   node capture.js https://example.com ./screenshots
 *   node capture.js https://example.com ./screenshots --routes /,/about,/pricing
 *   node capture.js https://site.figma.site ./screenshots --password mysecret
 *   node capture.js https://example.com ./screenshots --cookies cookies.json
 */

const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

async function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    baseUrl: args[0],
    outputDir: args[1],
    routes: ["/"],
    cookieFile: null,
    password: null,
    width: 1280,
    height: 1080,
  };

  for (let i = 2; i < args.length; i++) {
    switch (args[i]) {
      case "--routes":
        config.routes = args[++i].split(",").map((r) => r.trim());
        break;
      case "--cookies":
        config.cookieFile = args[++i];
        break;
      case "--password":
        config.password = args[++i];
        break;
      case "--width":
        config.width = parseInt(args[++i], 10);
        break;
      case "--height":
        config.height = parseInt(args[++i], 10);
        break;
    }
  }

  if (!config.baseUrl || !config.outputDir) {
    console.error(
      "Usage: node capture.js <base-url> <output-dir> [--routes r1,r2] [--cookies file] [--password pwd]"
    );
    process.exit(1);
  }

  return config;
}

function routeToFilename(route) {
  if (route === "/") return "homepage";
  return route
    .replace(/^\//, "")
    .replace(/\//g, "-")
    .replace(/[^a-zA-Z0-9-]/g, "_")
    .toLowerCase();
}

async function handlePasswordGate(page, password) {
  try {
    const passwordInput = await page.$(
      'input[type="password"], input[name="password"]'
    );
    if (passwordInput) {
      console.log("  Password gate detected, authenticating...");
      await passwordInput.fill(password);
      const submitBtn = await page.$(
        'button[type="submit"], input[type="submit"]'
      );
      if (submitBtn) {
        await submitBtn.click();
        await page.waitForLoadState("networkidle", { timeout: 15000 });
        await page.waitForTimeout(2000);
        return true;
      }
    }
  } catch (e) {
    console.error("  Password submission failed:", e.message);
  }
  return false;
}

async function captureScreenshots() {
  const config = await parseArgs();
  fs.mkdirSync(config.outputDir, { recursive: true });

  console.log(`Launching browser at ${config.width}x${config.height}...`);
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: config.width, height: config.height },
    deviceScaleFactor: 2,
  });

  // Load cookies if provided
  if (config.cookieFile && fs.existsSync(config.cookieFile)) {
    const cookies = JSON.parse(fs.readFileSync(config.cookieFile, "utf-8"));
    await context.addCookies(cookies);
    console.log(`Loaded cookies from ${config.cookieFile}`);
  }

  const page = await context.newPage();
  const results = [];

  // Handle password-protected sites on first load
  if (config.password) {
    console.log("Navigating to site for authentication...");
    await page.goto(config.baseUrl, {
      waitUntil: "networkidle",
      timeout: 30000,
    });
    await handlePasswordGate(page, config.password);
  }

  for (const route of config.routes) {
    const url = new URL(route, config.baseUrl).href;
    const filename = routeToFilename(route);
    const filepath = path.join(config.outputDir, `${filename}.png`);

    console.log(`Capturing: ${route} -> ${filename}.png`);

    try {
      await page.goto(url, { waitUntil: "networkidle", timeout: 30000 });
      // Wait for any animations to settle
      await page.waitForTimeout(1500);

      // Capture full-page screenshot
      await page.screenshot({
        path: filepath,
        fullPage: true,
      });

      // Get page dimensions for annotation coordinate mapping
      const dimensions = await page.evaluate(() => ({
        scrollWidth: document.documentElement.scrollWidth,
        scrollHeight: document.documentElement.scrollHeight,
        viewportWidth: window.innerWidth,
        viewportHeight: window.innerHeight,
      }));

      // Collect element positions for annotation targeting
      const elements = await page.evaluate(() => {
        const elMap = {};
        const selectors = [
          "nav",
          "header",
          "footer",
          "main",
          "form",
          "table",
          "button",
          '[role="button"]',
          'input:not([type="hidden"])',
          "select",
          "h1",
          "h2",
          "h3",
          '[class*="card"]',
          '[class*="chart"]',
          '[class*="sidebar"]',
          '[class*="tab"]',
          '[class*="modal"]',
          '[class*="alert"]',
          '[class*="toast"]',
          '[class*="empty"]',
          '[class*="holdings"]',
          '[class*="order"]',
          '[class*="price"]',
        ];

        for (const sel of selectors) {
          try {
            const nodes = document.querySelectorAll(sel);
            nodes.forEach((el, i) => {
              const rect = el.getBoundingClientRect();
              const scrollY = window.scrollY;
              const scrollX = window.scrollX;
              if (rect.width > 0 && rect.height > 0) {
                const key = `${sel}${nodes.length > 1 ? `[${i}]` : ""}`;
                elMap[key] = {
                  x: Math.round(rect.left + scrollX),
                  y: Math.round(rect.top + scrollY),
                  width: Math.round(rect.width),
                  height: Math.round(rect.height),
                  text: el.textContent?.slice(0, 80)?.trim() || "",
                };
              }
            });
          } catch (_) {}
        }
        return elMap;
      });

      results.push({
        route,
        filename: `${filename}.png`,
        filepath,
        dimensions,
        elements,
      });

      console.log(
        `  OK (${dimensions.scrollWidth}x${dimensions.scrollHeight}, ${Object.keys(elements).length} elements mapped)`
      );
    } catch (err) {
      console.error(`  FAILED: ${err.message}`);
      results.push({
        route,
        filename: `${filename}.png`,
        filepath: null,
        error: err.message,
      });
    }
  }

  // Save the element map for annotation use
  const manifestPath = path.join(config.outputDir, "capture-manifest.json");
  fs.writeFileSync(manifestPath, JSON.stringify(results, null, 2));
  console.log(`\nManifest saved to ${manifestPath}`);
  console.log(
    `Captured ${results.filter((r) => r.filepath).length}/${config.routes.length} screenshots`
  );

  await browser.close();
}

captureScreenshots().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
