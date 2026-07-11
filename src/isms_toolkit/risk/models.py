"""Data models for risk assessment (hobby ISMS toolkit)."""

from dataclasses import dataclass, field
from typing import Literal

Treatment = Literal["Mitigate", "Accept", "Transfer", "Avoid"]
RiskRating = Literal["Low", "Medium", "High", "Critical"]
Status = Literal["Open", "In Progress", "Closed", "Accepted"]


@dataclass
class RiskItem:
    id: str
    asset: str
    threat: str
    likelihood: int
    impact: int
    existing_controls: str = ""
    treatment: Treatment = "Mitigate"
    residual_likelihood: int | None = None
    residual_impact: int | None = None
    owner: str = ""
    review_date: str = ""
    status: Status = "Open"
    notes: str = ""

    # Computed on init / access
    inherent_score: int = field(init=False)
    inherent_rating: RiskRating = field(init=False)

    def __post_init__(self):
        from .calculator import calculate_inherent_risk

        self.inherent_score, self.inherent_rating = calculate_inherent_risk(
            self.likelihood, self.impact
        )
