#!/usr/bin/env python
"""One-command generation of all toolkit artifacts (risk + gap).

Run:
    python scripts/generate_all.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

def main():
    print("=== Generating Risk Register ===")
    subprocess.check_call([sys.executable, str(SCRIPTS / "generate_risk_register.py")])

    print("\n=== Generating Gap Analysis ===")
    subprocess.check_call([sys.executable, str(SCRIPTS / "generate_gap_analysis.py")])

    print("\n✅ All artifacts generated successfully.")
    print("Examples updated in examples/")

if __name__ == "__main__":
    main()
