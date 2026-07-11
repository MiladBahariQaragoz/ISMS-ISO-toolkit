# Aether Labs — Fictional Company Context (for ISMS examples)

**Name:** Aether Labs  
**Size:** ~22 people, remote-first (primarily EU)  
**Founded (fictional):** 2023  
**Product:** "Aether" — lightweight SaaS collaboration & task platform for small engineering teams (tasks, lightweight code review, async updates).

## ISMS Scope
The ISMS covers the design, development, operation, support, and hosting of the Aether SaaS platform together with all supporting internal information systems, processes, and third-party services used by Aether Labs staff.

In scope:
- Software development (Python backend, TypeScript/React frontend)
- Cloud infrastructure (AWS)
- Customer data processing (workspace data, some PII: names, emails, usage logs)
- Internal corporate systems (identity, finance light, HR tooling)
- Marketing site and public content

Out of scope (for this hobby example):
- Physical office security (remote-only)
- On-prem data centers
- Manufacturing / OT environments

## Key Information Assets
- Customer workspaces and associated data (confidentiality + integrity high)
- Source code and build artifacts (GitHub)
- CI/CD pipelines and secrets
- Internal identity and access systems
- Billing / customer account data (limited)
- Employee devices and SaaS accounts (M365, Slack, etc.)

## High-level Risk Context
- Heavy reliance on public cloud (AWS) and open-source dependencies
- Remote workforce (concentration of duties risks)
- Customer data protection obligations
- Small team → limited segregation in some processes
- Supply chain (npm, PyPI, GitHub Actions)
- Business continuity important for SaaS availability commitments

This context drives the example risk register, gap analysis statuses, and policy templates in the toolkit.
