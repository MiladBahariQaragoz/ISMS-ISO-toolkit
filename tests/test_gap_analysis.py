"""Basic tests for gap analysis logic (P3)."""

import json
from pathlib import Path

from isms_toolkit.gap.analysis import get_all_gaps, get_gap_status, summarize_gaps

ROOT = Path(__file__).resolve().parents[1]
CONTROLS = ROOT / "data" / "annex_a_controls.json"


def test_full_93_controls_loaded():
    controls = json.load(CONTROLS.open())
    assert len(controls) == 93
    themes = {c["theme"] for c in controls}
    assert themes == {"Organizational", "People", "Physical", "Technological"}


def test_gap_status_assignment():
    # Physical should default N/A for Aether
    assert get_gap_status("A.7.1", "Physical") == "Not Applicable"
    # Tech example
    status = get_gap_status("A.8.5", "Technological")
    assert status in ("Implemented", "Partially Implemented")


def test_get_all_gaps_and_summary():
    controls = json.load(CONTROLS.open())
    gaps = get_all_gaps(controls)
    assert len(gaps) == 93

    summary = summarize_gaps(gaps)
    assert summary["total"] == 93
    assert "Organizational" in summary["by_theme"]
