"""Risk scoring calculator for the ISMS hobby toolkit.

5x5 qualitative matrix (asset-based, common for small orgs).

Inherent risk = likelihood × impact
Ratings:
  1-4   Low
  5-9   Medium
  10-15 High
  16-25 Critical
"""

from typing import Literal

RiskRating = Literal["Low", "Medium", "High", "Critical"]
Treatment = Literal["Mitigate", "Accept", "Transfer", "Avoid"]


def validate_score(value: int) -> bool:
    if not isinstance(value, int) or not (1 <= value <= 5):
        raise ValueError("Score must be integer between 1 and 5")
    return True


def rating_from_score(score: int) -> RiskRating:
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Medium"
    if score <= 15:
        return "High"
    return "Critical"


def calculate_inherent_risk(likelihood: int, impact: int) -> tuple[int, RiskRating]:
    validate_score(likelihood)
    validate_score(impact)
    score = likelihood * impact
    rating = rating_from_score(score)
    return score, rating


def calculate_residual_risk(
    likelihood: int,
    impact: int,
    treatment: Treatment = "Mitigate",
) -> tuple[int, RiskRating]:
    """Very simple residual model for hobby purposes.

    Mitigate: roughly reduce by ~40-50% (clamped).
    Accept/Transfer/Avoid: return inherent (or 0 for Avoid in future).
    """
    validate_score(likelihood)
    validate_score(impact)
    score, _ = calculate_inherent_risk(likelihood, impact)

    if treatment == "Mitigate":
        reduced = max(1, int(score * 0.55))
    elif treatment == "Avoid":
        reduced = 1
    else:
        # Accept / Transfer — residual same as inherent for this simple model
        reduced = score

    return reduced, rating_from_score(reduced)
