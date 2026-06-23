#!/usr/bin/env python3
"""Create per-screen findings JSONs and annotate each screenshot."""
import json, subprocess, sys
from pathlib import Path

DIR = Path(__file__).parent / "screenshots"
SCRIPT = Path(__file__).parents[2] / ".claude/skills/ux-audit/scripts/annotate.py"

SEV = {
    1: "critical", 2: "critical",
    3: "high", 4: "high", 5: "high", 6: "high", 7: "high", 8: "high",
    9: "high", 10: "high", 11: "high", 12: "high", 13: "high",
    14: "medium", 15: "medium", 16: "medium", 17: "medium", 18: "medium",
    19: "medium", 20: "medium", 21: "medium", 22: "medium", 23: "medium", 24: "medium",
    25: "low", 26: "low",
}

# screen slug -> list of (finding number, x, y, short label)
PLACEMENTS = {
    "01-landing-overview-sgd": [
        (4, 760, 1010, "Upside-only marketing, no downside"),
        (5, 200, 1470, "Risk buried in collapsed FAQ"),
    ],
    "02-landing-overview-usd": [
        (11, 1180, 360, "Currency unit can switch silently"),
    ],
    "03-buy-trade-input": [
        (2, 1180, 720, "Error/validation states not on live screen"),
        (7, 300, 560, "Stale/conflicting price timestamp"),
        (14, 1370, 1230, "Weak, buried grey primary CTA"),
        (17, 1180, 840, "Unlabeled amount/quantity swap"),
    ],
    "04-review-buy-order": [
        (9, 180, 270, "Review vs Trade-detail near-identical"),
        (3, 1180, 300, "Indicative vs execution price gap"),
        (16, 780, 150, "No step indicator / header drift"),
        (12, 760, 850, "Cold liability-only copy at confirm"),
        (23, 600, 985, "Ambiguous 'Back' (discard or edit?)"),
        (8, 1410, 985, "No loading state on submit"),
    ],
    "05-trade-detail-confirmation": [
        (9, 180, 150, "Looks like Review; money moved?"),
        (15, 1050, 470, "Jargon undefined: Filled, Credit acct"),
        (21, 600, 1080, "Dead-end: no sell/download/alert"),
    ],
    "06-trade-history": [
        (11, 1060, 700, "SGD/USD/EUR mixed in rows"),
        (22, 300, 700, "Number/unit/account format drift"),
    ],
    "07-dashboard-holdings": [
        (13, 300, 620, "Alert count vs rows mismatch"),
    ],
    "08-dashboard-default": [
        (25, 900, 115, "Nav label drift: FX and treasury"),
    ],
    "10-modal-acknowledgement": [
        (6, 800, 545, "Unfilled token [6:00 AM SGT]"),
    ],
    "11-error-banner-specs": [
        (2, 370, 270, "Error states only as spec frames"),
        (19, 1050, 210, "Blocking vs warning look identical"),
    ],
    "12-push-noti-rate-reached": [
        (6, 190, 215, "Leaked delimiters <...SGD/ounce>"),
    ],
    "13-email-noti": [
        (6, 180, 300, "Unfilled merge fields <Surname>"),
    ],
    "15-terms-and-conditions": [
        (1, 800, 450, "Risk: T&Cs not openable, no KFS"),
        (18, 800, 300, "Duplicate account-creation message"),
    ],
    "16-confirmation-success": [
        (26, 800, 300, "Success message under-emphasised"),
        (8, 800, 230, "No processing state precedes this"),
        (24, 450, 985, "Back link vs button inconsistency"),
        (21, 1180, 985, "No 'place another trade'"),
    ],
    "18-buy-input-filled": [
        (18, 1180, 330, "New-account message redundant"),
        (20, 1180, 640, "Grey-on-grey labels; 0.00 ambiguity"),
    ],
    "19-sell-trade-input": [
        (10, 1180, 330, "Buy/Sell colour-only; red overloaded"),
    ],
}

for slug, items in PLACEMENTS.items():
    findings = [{"number": n, "severity": SEV[n], "x": x, "y": y, "label": lbl}
                for (n, x, y, lbl) in items]
    fpath = DIR / f"{slug}-findings.json"
    fpath.write_text(json.dumps(findings, indent=2))
    inp = DIR / f"{slug}.png"
    out = DIR / f"{slug}-annotated.png"
    r = subprocess.run([sys.executable, str(SCRIPT), str(inp), str(fpath), str(out)],
                       capture_output=True, text=True)
    status = "OK" if r.returncode == 0 else f"FAIL: {r.stderr.strip()}"
    print(f"{slug}: {len(findings)} markers -> {status}")
