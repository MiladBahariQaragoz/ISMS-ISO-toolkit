# ISMS ISO Toolkit

A personal hobby project: Python automation for ISO 27001:2022 risk registers, Annex A gap analysis, policy templates, and control mapping — using a realistic fictional small company.

All examples and artifacts are built for **Aether Labs** (a made-up 22-person remote-first SaaS company). The goal is learning by producing clean, usable GRC artifacts and the code that generates them.

## What it produces

1. **Risk register tool** — Python + Excel. Asset inventory, threat/vulnerability pairs, 5×5 likelihood × impact scoring, treatment plans, residual risk, and a visual heatmap.
2. **Annex A (2022) gap analysis** — Full 93-control checklist with realistic statuses for the fictional company, theme summaries, and a Statement of Applicability excerpt.
3. **Policy pack** — 7 practical Markdown policy templates (Information Security, Acceptable Use, Access Control, Incident Management, Business Continuity, Supplier Security, Data Protection).
4. **Control mapping** — How common technical and operational practices map to ISO 27001 controls (with notes on NIST CSF 2.0 and BSI Grundschutz).
5. **Streamlit dashboard** — Interactive explorer for the generated risk and gap data.

Everything is data-driven and reproducible.

## Quick start (once built)

```bash
# after setup
python -m scripts.generate_all
streamlit run dashboard/app.py
```

See `docs/implementation-plan.md` for the full architecture, data model, and verification steps.

## Fictional company

**Aether Labs** — remote EU team of ~22 building a lightweight SaaS collaboration platform ("Aether") for small engineering teams. Heavy AWS + modern dev tooling, customer data with some PII, open source dependencies, remote workforce.

See `data/company_context.md` (after Phase 0) for the full scope and asset picture used across all artifacts.

## Project status

Early stage. Follow the implementation plan in `docs/implementation-plan.md` for traceable phases (P0–P8), each with Definition of Success and verification checklists.

See also:
- `docs/methodology.md` (once written)
- `docs/control-mapping.md`

## Why hobby?

Built for personal understanding of ISMS mechanics, risk methodology, and turning dry compliance work into something automated and visual. All content stays educational and fictional.

## License

MIT (hobby / personal use friendly).

## Contributing

This is a personal project. Issues and PRs for improvements are welcome but not expected.

## Learning resources used

- ISO/IEC 27001:2022 & 27002
- NIST CSF 2.0
- Common risk register patterns (5×5 qualitative)
- Public Annex A control references

Contributions that improve accuracy or usability are appreciated.
