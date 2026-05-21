#!/usr/bin/env python3
"""Export all top-level frames from a Figma file as PNG images.

Usage:
    python3 figma_export.py <figma-url> <output-dir> --token <PAT>
    python3 figma_export.py <figma-url> <output-dir> --token-env FIGMA_TOKEN

Arguments:
    figma-url    Figma file URL (with optional node-id query param)
    output-dir   Directory to save exported PNGs
    --token      Figma Personal Access Token (inline)
    --token-env  Environment variable containing the token
    --scale      Export scale factor (default: 2)
    --format     Export format: png, jpg, svg, pdf (default: png)
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_figma_url(url: str) -> Tuple[str, Optional[str]]:
    """Extract file key and node ID from a Figma URL."""
    # Match: figma.com/design/<key>/... or figma.com/file/<key>/...
    match = re.search(r'figma\.com/(?:design|file)/([a-zA-Z0-9]+)', url)
    if not match:
        print(f"Error: Could not extract file key from URL: {url}", file=sys.stderr)
        sys.exit(1)
    file_key = match.group(1)

    # Extract node-id from query params if present
    node_id = None
    node_match = re.search(r'node-id=([0-9]+-[0-9]+)', url)
    if node_match:
        node_id = node_match.group(1).replace('-', ':')

    return file_key, node_id


def figma_api(endpoint: str, token: str) -> Dict[str, Any]:
    """Make a GET request to the Figma REST API."""
    url = f"https://api.figma.com/v1{endpoint}"
    req = urllib.request.Request(url, headers={"X-Figma-Token": token})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.readable() else ""
        print(f"Error: Figma API {e.code} on {endpoint}: {body}", file=sys.stderr)
        sys.exit(1)


def collect_top_frames(node: Dict[str, Any], depth: int = 0) -> List[Dict[str, Any]]:
    """Collect top-level frame/component nodes (direct children of a page or section)."""
    frames = []
    node_type = node.get("type", "")

    # If this is a CANVAS (page) or SECTION, collect its direct frame children
    if node_type in ("CANVAS", "SECTION", "DOCUMENT") or depth == 0:
        for child in node.get("children", []):
            child_type = child.get("type", "")
            if child_type in ("FRAME", "COMPONENT", "COMPONENT_SET", "INSTANCE", "GROUP", "SECTION"):
                if child_type == "SECTION":
                    # Recurse into sections to find frames inside
                    frames.extend(collect_top_frames(child, depth + 1))
                else:
                    frames.append({
                        "id": child["id"],
                        "name": child.get("name", f"frame-{child['id']}"),
                        "type": child_type,
                    })
    return frames


def slugify(name: str) -> str:
    """Convert a frame name to a filename-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug or "unnamed"


def download_file(url: str, dest: Path) -> None:
    """Download a file from URL to destination path."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        dest.write_bytes(resp.read())


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Figma frames as images")
    parser.add_argument("figma_url", help="Figma file URL")
    parser.add_argument("output_dir", help="Output directory for exported images")
    parser.add_argument("--token", help="Figma Personal Access Token")
    parser.add_argument("--token-env", help="Env var containing Figma PAT")
    parser.add_argument("--scale", type=int, default=2, help="Export scale (default: 2)")
    parser.add_argument("--format", default="png", choices=["png", "jpg", "svg", "pdf"],
                        help="Export format (default: png)")
    args = parser.parse_args()

    # Resolve token
    token = args.token
    if not token and args.token_env:
        token = os.environ.get(args.token_env)
    if not token:
        token = os.environ.get("FIGMA_TOKEN")
    if not token:
        print("Error: No Figma token provided. Use --token, --token-env, or set FIGMA_TOKEN.", file=sys.stderr)
        sys.exit(1)

    # Parse URL
    file_key, node_id = parse_figma_url(args.figma_url)
    print(f"File key: {file_key}")
    print(f"Node ID: {node_id or '(entire file)'}")

    # Create output directory
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Fetch file/node structure
    if node_id:
        print(f"Fetching node {node_id}...")
        data = figma_api(f"/files/{file_key}/nodes?ids={node_id}", token)
        root_node = data["nodes"][node_id]["document"]
    else:
        print("Fetching full file structure...")
        data = figma_api(f"/files/{file_key}", token)
        root_node = data["document"]

    # Collect frames (filter out utility elements)
    SKIP_NAMES = {"Annotation", "Flow Subheader", "Logic", "Tertiary Dropdown - Single"}
    all_frames = collect_top_frames(root_node)
    frames = [f for f in all_frames if f["name"] not in SKIP_NAMES
              and not f["name"].startswith("Annotation")]
    if not frames:
        print("Error: No frames found in the specified node.", file=sys.stderr)
        print("Node structure:", json.dumps(root_node, indent=2)[:2000], file=sys.stderr)
        sys.exit(1)

    print(f"\nFound {len(frames)} frames:")
    for i, f in enumerate(frames, 1):
        print(f"  {i}. {f['name']} ({f['type']}, id: {f['id']})")

    # Request image exports (batch — up to 50 IDs per request)
    batch_size = 10
    all_images: Dict[str, str] = {}

    for batch_start in range(0, len(frames), batch_size):
        batch = frames[batch_start:batch_start + batch_size]
        ids_param = ",".join(f["id"] for f in batch)
        print(f"\nRequesting exports for {len(batch)} frames (scale={args.scale}x, format={args.format})...")
        images_data = figma_api(
            f"/images/{file_key}?ids={ids_param}&scale={args.scale}&format={args.format}",
            token
        )
        if images_data.get("err"):
            print(f"Warning: API returned error: {images_data['err']}", file=sys.stderr)
        all_images.update(images_data.get("images", {}))

    # Download images
    manifest = []
    seen_slugs: Dict[str, int] = {}

    for i, frame in enumerate(frames, 1):
        image_url = all_images.get(frame["id"])
        if not image_url:
            print(f"  Skipping {frame['name']} — no image URL returned")
            continue

        slug = slugify(frame["name"])
        # Handle duplicate slugs
        if slug in seen_slugs:
            seen_slugs[slug] += 1
            slug = f"{slug}-{seen_slugs[slug]}"
        else:
            seen_slugs[slug] = 1

        filename = f"{slug}.{args.format}"
        dest = out_dir / filename
        print(f"  [{i}/{len(frames)}] Downloading {frame['name']} → {filename}...")
        try:
            download_file(image_url, dest)
            file_size = dest.stat().st_size
            print(f"    ✓ {file_size:,} bytes")
            manifest.append({
                "id": frame["id"],
                "name": frame["name"],
                "type": frame["type"],
                "filename": filename,
                "slug": slug,
                "flow_order": i,
                "file_size": file_size,
            })
        except Exception as e:
            print(f"    ✗ Download failed: {e}", file=sys.stderr)

        # Brief pause to avoid rate limits
        if i < len(frames):
            time.sleep(0.2)

    # Save manifest
    manifest_path = out_dir / "screen-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"\nDone! Exported {len(manifest)}/{len(frames)} frames to {out_dir}")
    print(f"Manifest saved to {manifest_path}")


if __name__ == "__main__":
    main()
