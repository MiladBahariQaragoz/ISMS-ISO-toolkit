# Methodology

This document explains the approach used in the ISMS ISO Toolkit for a fictional company (Aether Labs). It is intended for educational and learning purposes.

## Risk Assessment Approach

The toolkit uses a qualitative, asset-based risk assessment method aligned with common practices for small organizations under ISO 27001 / ISO 27005 guidance.

- **Asset Identification**: Key information assets are defined in `data/assets.yaml` and the risk seed.
- **Threat and Vulnerability Pairing**: Each risk item combines a threat with a vulnerability affecting an asset.
- **Likelihood and Impact**: Both scored on a 1–5 scale.
- **Inherent Risk Score**: Calculated as `likelihood × impact`.
- **Risk Rating Bands**:
  - 1–4: Low (green)
  - 5–9: Medium (yellow)
  - 10–15: High (orange)
  - 16–25: Critical (red)
- **Treatment Options**: Mitigate (Treat), Accept, Transfer, Avoid.
- **Residual Risk**: Simple reduction applied for "Mitigate" (approximately 45% reduction in the model); other treatments retain or minimize the score.

**Why 5×5?**  
It is widely understood, easy to communicate to non-technical stakeholders, and sufficient for small-to-medium organizations. It supports consistent decision-making without requiring complex quantitative data.

## How the Generators Work

### Risk Register (`scripts/generate_risk_register.py`)
- Loads seed data from `data/risk_register_seed.yaml`.
- Uses pure functions in `src/isms_toolkit/risk/calculator.py` to compute scores and ratings.
- Builds a multi-sheet Excel workbook via `openpyxl`:
  - Document Control (versioning and hobby markers)
  - Risk Register (detailed table with conditional formatting)
  - Heatmap (5×5 count matrix + Top 5 risks list)
  - Summary (counts by rating)

### Gap Analysis (`scripts/generate_gap_analysis.py`)
- Loads full Annex A controls from `data/annex_a_controls.json` (93 controls).
- Applies realistic status logic in `src/isms_toolkit/gap/analysis.py` tailored to a remote SaaS company:
  - Physical controls → mostly "Not Applicable"
  - Organizational/People → mostly "Partially Implemented"
  - Technological → mix, stronger in dev practices
- Generates:
  - Annex A Controls checklist (colored status, filters, freeze panes)
  - Summary by theme
  - Statement of Applicability (excerpt)

All outputs are deterministic and reproducible from the data files.

## Limitations of This Hobby Toolkit

- **Qualitative only**: No monetary loss estimates or advanced quantitative methods (e.g., FAIR).
- **Static seeds**: Risk and gap data are example snapshots, not dynamically updated from real systems.
- **Simplified residual risk**: The reduction model is illustrative, not calibrated to real control effectiveness.
- **No full ISMS**: Missing elements such as internal audit program, management review records, training logs, or continuous monitoring.
- **Fictional scope**: Everything is built around "Aether Labs" for demonstration. Real organizations must tailor to their context, legal requirements, and risk appetite.
- **Educational focus**: Policies and artifacts are templates. They require review, approval, and customization before any operational use.

This toolkit demonstrates *how* to structure and automate ISMS artifacts, not a production-ready compliance platform.

## How to Adapt for Real Use

1. Replace `data/company_context.md` and seed files with your organization's assets, threats, and controls.
2. Adjust risk scoring bands and residual calculation to match your methodology.
3. Expand or replace status logic in gap analysis based on actual control implementation evidence.
4. Customize policies with your organization's name, roles, and specific requirements.
5. Add versioning, approval workflows, and document control records suitable for audit.
6. Integrate with real data sources (e.g., asset management tools, vulnerability scanners) if automation is expanded.
7. Conduct formal risk assessments and gap analyses with subject-matter experts and management.

The modular structure (`data/`, `src/isms_toolkit/{risk,gap,excel}/`, `policies/`) is designed to support such extensions.

## References
- ISO/IEC 27001:2022
- ISO/IEC 27002:2022
- ISO/IEC 27005 (risk management guidance)
- ENISA and common GRC practice for 5×5 matrices

This methodology was developed as part of a personal hobby project to explore practical implementation of ISO 27001 concepts.
