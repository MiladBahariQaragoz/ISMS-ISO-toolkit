"""Tests for risk calculator (TDD style).

Run with: pytest tests/test_risk_calculator.py -q
"""

import pytest

# Expected public API (will implement in src/isms_toolkit/risk/calculator.py)
from isms_toolkit.risk.calculator import (
    calculate_inherent_risk,
    calculate_residual_risk,
    rating_from_score,
    validate_score,
)


def test_validate_score_valid():
    assert validate_score(1) is True
    assert validate_score(5) is True


def test_validate_score_invalid():
    with pytest.raises(ValueError):
        validate_score(0)
    with pytest.raises(ValueError):
        validate_score(6)


def test_calculate_inherent_basic():
    score, rating = calculate_inherent_risk(3, 4)
    assert score == 12
    assert rating == "High"


def test_calculate_inherent_low():
    score, rating = calculate_inherent_risk(1, 2)
    assert score == 2
    assert rating == "Low"


def test_calculate_inherent_critical():
    score, rating = calculate_inherent_risk(5, 5)
    assert score == 25
    assert rating == "Critical"


def test_rating_from_score_bands():
    assert rating_from_score(1) == "Low"
    assert rating_from_score(4) == "Low"
    assert rating_from_score(5) == "Medium"
    assert rating_from_score(9) == "Medium"
    assert rating_from_score(10) == "High"
    assert rating_from_score(15) == "High"
    assert rating_from_score(16) == "Critical"
    assert rating_from_score(25) == "Critical"


def test_calculate_residual_simple():
    # After treatment, risk reduced
    residual_score, residual_rating = calculate_residual_risk(
        likelihood=3, impact=4, treatment="Mitigate"
    )
    assert residual_score < 12
    assert residual_rating in ("Medium", "High")


def test_calculate_residual_accept():
    score, rating = calculate_residual_risk(3, 3, treatment="Accept")
    assert score == 9
    assert rating == "Medium"


def test_full_risk_item_smoke():
    # Placeholder for later integration with seeds
    from isms_toolkit.risk.models import RiskItem

    item = RiskItem(
        id="R-TEST",
        asset="Test asset",
        threat="Test threat",
        likelihood=3,
        impact=4,
        treatment="Mitigate",
    )
    assert item.inherent_score == 12
    assert item.inherent_rating == "High"
