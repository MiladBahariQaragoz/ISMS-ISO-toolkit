# 06 — ISMS-in-a-Box: ISO 27001 / Risk & Compliance Toolkit

**Difficulty:** ⭐⭐⭐ · **Est. effort:** 3–4 weeks · **Repo name idea:** `isms-in-a-box`

## Why this project
This covers the **governance/GRC half of the demand that pure technical projects miss**:
**compliance (35%)**, **risk assessment (32%)**, **ISO 27001 (8%)**, security policies,
governance. Many German roles (IT Security Coordinator — the #1 role title in your data,
12 postings; Consultant; Working Student GRC) are **GRC-heavy, not hands-on-hacking**. This
makes you credible for them.

## Skills this proves (put on CV)
- **Risk assessment & risk management** (methodology, risk register)
- **Compliance** & **ISO 27001 / NIST CSF** familiarity
- **Security policies** & governance (ISMS documentation)
- Security **audits** & gap analysis

## Scope / what you build
A practical, reusable **GRC toolkit** + a worked example ISMS for a fictional small company —
part documents, part automation.

1. **Risk register (automation):** a Python/Excel-driven **risk assessment** tool —
   asset inventory → threats → likelihood × impact → risk score → treatment plan. Output a
   clean risk register and a heat-map.
2. **ISO 27001 gap analysis:** a checklist mapping the **Annex A (2022) controls** to
   "implemented / partial / missing" for the fictional company, with evidence notes.
3. **Policy pack:** write real, usable policy templates — Information Security Policy,
   Access Control, Acceptable Use, Incident Response, BCP/DR, supplier security.
4. **Control mapping:** cross-map your technical projects (01 hardening, 03 IR, 05 pipeline)
   to the ISO 27001 / NIST CSF / **BSI Grundschutz** controls they satisfy — this *ties your
   whole portfolio together* and shows you connect tech to governance.
5. **Bonus:** a small Streamlit dashboard over the risk register.

## Definition of done
- [ ] Public repo: risk-assessment tool + sample risk register + heat-map.
- [ ] ISO 27001 Annex A gap-analysis spreadsheet for the example company.
- [ ] 5+ written policy templates.
- [ ] A control-mapping doc linking your other Sec-CV projects to framework controls.

## Build order
1. Read ISO 27001/27002 structure + NIST CSF; learn the control families.
2. Build the risk-register tool; populate it for the fictional company.
3. Run the Annex A gap analysis.
4. Write the policy pack; build the cross-project control map.

## Learning resources
- ISO/IEC 27001:2022 & 27002 overviews, NIST CSF 2.0, **BSI IT-Grundschutz** (German market!).
- ENISA risk-management guidance; OpenFAIR for quantitative risk (optional).
- Consider a **CISM/ISO 27001 Foundation** awareness course later.

## CV bullet (target)
> Built an ISMS toolkit — a Python risk-assessment/register tool, an ISO 27001:2022 Annex A
> gap analysis, and a policy pack — and mapped technical controls to ISO 27001 / NIST CSF /
> BSI Grundschutz for a sample organisation.
