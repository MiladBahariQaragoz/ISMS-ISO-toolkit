#!/usr/bin/env python
"""Generate risk register Excel from seed (hobby toolkit)."""

import sys
from pathlib import Path

import yaml

# allow running without install
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from isms_toolkit.excel.risk_workbook import create_risk_workbook, save_workbook

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "data" / "risk_register_seed.yaml"
OUT_DIR = ROOT / "outputs"
EXAMPLE = ROOT / "examples"


def main():
    data = yaml.safe_load(SEED.read_text())
    risks = data.get("risks", [])
    wb = create_risk_workbook(risks, company="Aether Labs")
    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / "risk-register-aether-labs.xlsx"
    save_workbook(wb, out_path)

    # also copy to examples for committed sample
    EXAMPLE.mkdir(exist_ok=True)
    save_workbook(wb, EXAMPLE / "risk-register-aether-labs.xlsx")
    print("Risk register generation complete.")


if __name__ == "__main__":
    main()
