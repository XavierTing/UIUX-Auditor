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

Severity colours:
    critical = red (#DC2626)
    high     = orange (#EA580C)
    medium   = yellow (#CA8A04)
    low      = green (#16A34A)
"""

import json
import sys
import os
from PIL import Image, ImageDraw, ImageFont

SEVERITY_COLOURS = {
    "critical": (220, 38, 38),      # Red
    "high":     (234, 88, 12),      # Orange
    "medium":   (202, 138, 4),      # Yellow/Amber
    "low":      (22, 163, 74),      # Green
}

SEVERITY_LABELS = {
    "critical": "CRITICAL",
    "high":     "HIGH",
    "medium":   "MEDIUM",
    "low":      "LOW",
}

MARKER_RADIUS = 28
MARKER_BORDER = 4
SHADOW_OFFSET = 3
LEGEND_HEIGHT = 80
LEGEND_PADDING = 24


def get_font(size):
    """Try to load a bold font, fall back to default."""
    font_paths = [
        "/System/Library/Fonts/SFNSTextCondensed-Bold.otf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
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
    """Draw a numbered circle marker with severity colour coding."""
    colour = SEVERITY_COLOURS.get(severity, (128, 128, 128))
    r = MARKER_RADIUS

    # Drop shadow
    draw.ellipse(
        [x - r + SHADOW_OFFSET, y - r + SHADOW_OFFSET,
         x + r + SHADOW_OFFSET, y + r + SHADOW_OFFSET],
        fill=(0, 0, 0, 80)
    )

    # White border ring
    draw.ellipse(
        [x - r - MARKER_BORDER, y - r - MARKER_BORDER,
         x + r + MARKER_BORDER, y + r + MARKER_BORDER],
        fill=(255, 255, 255)
    )

    # Coloured circle
    draw.ellipse([x - r, y - r, x + r, y + r], fill=colour)

    # Number text (centered)
    text = str(number)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(
        (x - tw / 2, y - th / 2 - 1),
        text,
        fill=(255, 255, 255),
        font=font,
    )


def draw_legend(img, findings):
    """Append a severity legend bar at the bottom of the image."""
    width = img.width
    legend = Image.new("RGBA", (width, LEGEND_HEIGHT), (255, 255, 255, 240))
    draw = ImageDraw.Draw(legend)

    font_label = get_font(16)
    font_title = get_font(18)

    # Title
    draw.text((LEGEND_PADDING, 8), "AUDIT FINDINGS", fill=(0, 0, 0), font=font_title)

    # Count by severity
    counts = {}
    for f in findings:
        sev = f.get("severity", "medium")
        counts[sev] = counts.get(sev, 0) + 1

    # Draw legend items
    x_offset = LEGEND_PADDING
    y_pos = 32
    for sev in ["critical", "high", "medium", "low"]:
        if sev not in counts:
            continue
        colour = SEVERITY_COLOURS[sev]
        label = f"{SEVERITY_LABELS[sev]} ({counts[sev]})"

        # Colour dot
        draw.ellipse([x_offset, y_pos, x_offset + 12, y_pos + 12], fill=colour)

        # Label
        draw.text((x_offset + 18, y_pos - 1), label, fill=(50, 50, 50), font=font_label)

        bbox = draw.textbbox((0, 0), label, font=font_label)
        x_offset += 18 + (bbox[2] - bbox[0]) + 24

    # Separator line
    draw.line([(0, 0), (width, 0)], fill=(200, 200, 200), width=1)

    # Composite legend onto image
    result = Image.new("RGBA", (width, img.height + LEGEND_HEIGHT))
    result.paste(img, (0, 0))
    result.paste(legend, (0, img.height))
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
    font = get_font(22)
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
