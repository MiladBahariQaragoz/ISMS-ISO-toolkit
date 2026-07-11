"""Gap analysis logic for ISO 27001 Annex A (hobby toolkit).

Provides realistic statuses for the fictional Aether Labs (remote SaaS).
"""


# Realistic status distribution for a small remote tech/SaaS company
# Physical controls are largely N/A or low maturity
# Org and People: mostly partial
# Tech: stronger in dev practices, partial elsewhere

DEFAULT_STATUS_BY_THEME = {
    "Organizational": "Partially Implemented",
    "People": "Partially Implemented",
    "Physical": "Not Applicable",
    "Technological": "Partially Implemented",
}

# Specific overrides for Aether Labs (example realistic picture)
SPECIFIC_STATUSES: dict[str, str] = {
    # Stronger tech / dev practices
    "A.8.5": "Implemented",   # Secure authentication
    "A.8.7": "Implemented",   # Protection against malware
    "A.8.9": "Implemented",   # Configuration management (good IaC)
    "A.8.20": "Implemented",  # Networks security
    "A.8.25": "Partially Implemented",  # Secure SDLC
    "A.8.28": "Implemented",  # Secure coding (we try)
    # Org / policy gaps (small team)
    "A.5.1": "Partially Implemented",
    "A.5.9": "Implemented",   # Asset inventory (we have some)
    "A.5.15": "Partially Implemented",
    "A.5.19": "Partially Implemented",
    # Physical mostly N/A
    "A.7.1": "Not Applicable",
    "A.7.7": "Not Applicable",
    # People
    "A.6.3": "Partially Implemented",  # Awareness
    "A.6.7": "Implemented",   # Remote working (core to business)
}

STATUS_OPTIONS = ["Implemented", "Partially Implemented", "Not Implemented", "Not Applicable"]


def get_gap_status(control_id: str, theme: str) -> str:
    if control_id in SPECIFIC_STATUSES:
        return SPECIFIC_STATUSES[control_id]
    return DEFAULT_STATUS_BY_THEME.get(theme, "Partially Implemented")


def get_all_gaps(controls: list[dict]) -> list[dict]:
    """Return list of gap items with status and notes for Aether Labs."""
    gaps = []
    for c in controls:
        status = get_gap_status(c["id"], c["theme"])
        notes = ""
        if status == "Partially Implemented":
            notes = "Some controls in place; documentation or consistency gaps remain."
        elif status == "Not Applicable":
            notes = "Remote-only company; physical controls do not apply to scope."
        elif status == "Implemented":
            notes = "Core practice in place for Aether Labs operations."
        gaps.append({
            "id": c["id"],
            "theme": c["theme"],
            "title": c["title"],
            "status": status,
            "notes": notes,
            "owner": "Platform" if c["theme"] == "Technological" else "Management",
            "priority": (
                "High"
                if status in ("Not Implemented", "Partially Implemented")
                and c["theme"] != "Physical"
                else "Low"
            ),
        })
    return gaps


def summarize_gaps(gaps: list[dict]) -> dict:
    """Return summary counts by theme and overall."""
    summary = {"by_theme": {}, "total": len(gaps)}
    for g in gaps:
        t = g["theme"]
        s = g["status"]
        if t not in summary["by_theme"]:
            summary["by_theme"][t] = {
                "Implemented": 0,
                "Partially Implemented": 0,
                "Not Implemented": 0,
                "Not Applicable": 0,
            }
        summary["by_theme"][t][s] = summary["by_theme"][t].get(s, 0) + 1
    return summary
