#!/usr/bin/env python3
"""
Screenshot Annotation Script for UX Audit

Takes a screenshot + findings JSON and draws numbered severity markers.

Usage:
    python3 annotate.py <input-image> <findings-json> <output-image>

findings.json format:
[
    {
        "number": 1,
        "severity": "critical",
        "x": 640,
        "y": 200,
        "label": "No onboarding for novice users"
    },
    ...
]

Severity colours (Anthropic-Research earthy palette):
    critical = terracotta (#B5481F)
    high     = ochre      (#A6680A)
    medium   = olive      (#7B6E14)
    low      = moss       (#4B6F44)
"""

import json
import sys
import os
from PIL import Image, ImageDraw, ImageFont

SEVERITY_COLOURS = {
    "critical": (181, 72, 31),      # Terracotta — #B5481F
    "high":     (166, 104, 10),     # Ochre      — #A6680A
    "medium":   (123, 110, 20),     # Olive      — #7B6E14
    "low":      (75, 111, 68),      # Moss       — #4B6F44
}

SEVERITY_LABELS = {
    "critical": "CRITICAL",
    "high":     "HIGH",
    "medium":   "MEDIUM",
    "low":      "LOW",
}

MARKER_RADIUS = 12               # legacy clamp used by annotate() offset math
MARKER_BORDER = 1                # cream ring thickness around the pill
RING_COLOUR = (250, 249, 245)    # Cream #FAF9F5 — matches report background
PILL_HEIGHT = 22
PILL_HPAD = 7                    # horizontal padding inside the pill, each side
PILL_MIN_WIDTH = 24
PILL_RADIUS_OUTER = 4
PILL_RADIUS_INNER = 3

LEGEND_HEIGHT = 36
LEGEND_TOP_GAP = 20              # cream padding between screenshot bottom and legend strip
LEGEND_PADDING = 24
LEGEND_BG = (250, 249, 245, 255) # cream — matches report
LEGEND_TEXT = (107, 106, 99)     # warm muted grey — matches --muted in CSS


def get_font(size):
    """Try to load a mono/sans body font, fall back to default."""
    font_paths = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Supplemental/Menlo.ttc",
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def get_bold_font(size):
    """Bold mono font for the marker numeral. Tries Menlo Bold (index 1 of
    Menlo.ttc) first, then standalone bold-mono fonts, then bold-sans fallback."""
    # .ttc collections — pass explicit index for Bold variant
    # macOS Menlo.ttc order: 0=Regular, 1=Bold, 2=Italic, 3=Bold-Italic
    ttc_candidates = [
        ("/System/Library/Fonts/Menlo.ttc", 1),
        ("/System/Library/Fonts/Supplemental/Menlo.ttc", 1),
    ]
    for path, idx in ttc_candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=idx)
            except Exception:
                continue

    font_paths = [
        "/Library/Fonts/SF-Mono-Bold.otf",
        "/System/Library/Fonts/Supplemental/SF-Mono-Bold.otf",
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_marker(draw, x, y, number, severity, font):
    """Draw a pill-shaped numbered marker — mirrors the HTML .finding-badge."""
    colour = SEVERITY_COLOURS.get(severity, (107, 106, 99))

    text = str(number)
    # Measure with anchor='lt' so we get the actual visual width for pill sizing
    bbox = draw.textbbox((0, 0), text, font=font, anchor='lt')
    tw = bbox[2] - bbox[0]

    pill_w = max(PILL_MIN_WIDTH, tw + 2 * PILL_HPAD)
    half_w = pill_w / 2
    half_h = PILL_HEIGHT / 2

    # Cream hairline ring (1 px outside the pill)
    draw.rounded_rectangle(
        [x - half_w - MARKER_BORDER, y - half_h - MARKER_BORDER,
         x + half_w + MARKER_BORDER, y + half_h + MARKER_BORDER],
        radius=PILL_RADIUS_OUTER, fill=RING_COLOUR,
    )

    # Coloured pill
    draw.rounded_rectangle(
        [x - half_w, y - half_h, x + half_w, y + half_h],
        radius=PILL_RADIUS_INNER, fill=colour,
    )

    # Number — anchor='mm' centers the text middle-middle at (x, y) using
    # the font's actual ascent/descent, not the ink bounding box. This keeps
    # 1, 2, 8, 22 etc. all visually centered in the same pill.
    draw.text(
        (x, y),
        text,
        fill=(255, 255, 255),
        font=font,
        anchor='mm',
    )


def draw_legend(img, findings):
    """Append a compact, single-line severity legend below the screenshot,
    with a cream gap above it so the legend reads as report chrome, not part
    of the underlying UI."""
    width = img.width

    # Compact one-line legend on a cream background — matches report --muted.
    legend = Image.new("RGBA", (width, LEGEND_HEIGHT), LEGEND_BG)
    draw = ImageDraw.Draw(legend)

    font_label = get_font(11)
    font_title = get_font(11)

    # Title (small mono eyebrow)
    title_y = 12
    draw.text((LEGEND_PADDING, title_y), "FINDINGS", fill=LEGEND_TEXT, font=font_title)

    counts = {}
    for f in findings:
        sev = f.get("severity", "medium")
        counts[sev] = counts.get(sev, 0) + 1

    # Severity dots + counts laid out inline to the right of the title.
    x_offset = LEGEND_PADDING + 110
    for sev in ["critical", "high", "medium", "low"]:
        if sev not in counts:
            continue
        colour = SEVERITY_COLOURS[sev]
        label = f"{SEVERITY_LABELS[sev]} ({counts[sev]})"

        # Small severity dot (7 px) vertically centred with the text
        dot_top = title_y + 4
        draw.ellipse([x_offset, dot_top, x_offset + 7, dot_top + 7], fill=colour)

        draw.text((x_offset + 12, title_y - 1), label, fill=LEGEND_TEXT, font=font_label)

        bbox = draw.textbbox((0, 0), label, font=font_label)
        x_offset += 12 + (bbox[2] - bbox[0]) + 20

    # Composite: screenshot + cream gap + legend strip.
    result = Image.new(
        "RGBA",
        (width, img.height + LEGEND_TOP_GAP + LEGEND_HEIGHT),
        LEGEND_BG,
    )
    result.paste(img, (0, 0))
    result.paste(legend, (0, img.height + LEGEND_TOP_GAP))
    return result


def annotate(input_path, findings_path, output_path):
    """Main annotation function."""
    # Load image
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Load findings
    with open(findings_path, "r") as f:
        findings = json.load(f)

    if not findings:
        print(f"No findings to annotate on {input_path}")
        img.save(output_path)
        return

    # Draw connector lines from marker to component area (subtle)
    font = get_bold_font(14)
    for finding in findings:
        x = finding["x"]
        y = finding["y"]
        number = finding["number"]
        severity = finding.get("severity", "medium")

        # Offset marker to top-left corner of the component, slightly outside
        marker_x = max(MARKER_RADIUS + MARKER_BORDER + 5, x - 10)
        marker_y = max(MARKER_RADIUS + MARKER_BORDER + 5, y - 10)

        draw_marker(draw, marker_x, marker_y, number, severity, font)

    # Composite overlay onto image
    img = Image.alpha_composite(img, overlay)

    # Add legend
    img = draw_legend(img, findings)

    # Save
    img = img.convert("RGB")
    img.save(output_path, quality=95)
    print(f"Annotated: {output_path} ({len(findings)} markers)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 annotate.py <input-image> <findings-json> <output-image>")
        sys.exit(1)

    annotate(sys.argv[1], sys.argv[2], sys.argv[3])
