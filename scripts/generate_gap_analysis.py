#!/usr/bin/env python
"""Generate Annex A gap analysis Excel (hobby toolkit)."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from isms_toolkit.excel.gap_workbook import create_gap_workbook, save_workbook

ROOT = Path(__file__).resolve().parents[1]
CONTROLS = ROOT / "data" / "annex_a_controls.json"
OUT_DIR = ROOT / "outputs"
EXAMPLE = ROOT / "examples"


def main():
    controls = json.load(CONTROLS.open())
    wb = create_gap_workbook(controls, company="Aether Labs")

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / "gap-analysis-aether-labs.xlsx"
    save_workbook(wb, out)

    EXAMPLE.mkdir(exist_ok=True)
    save_workbook(wb, EXAMPLE / "gap-analysis-aether-labs.xlsx")
    print("Gap analysis generation complete.")


if __name__ == "__main__":
    main()
