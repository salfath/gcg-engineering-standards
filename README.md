# GCG Engineering Standards

**Status:** Draft v0.1.0 — pending GCG Engineering Lead approval.  
**Scope:** Scola, Salus, CBT, Akor, Prima, and future GCG products.

This is the technology-neutral engineering handbook. **MUST** = mandatory; **SHOULD** = recommended unless an exception is documented; **MAY** = optional.

## Start here
1. [Governance](docs/01-governance.md)
2. [Local development](docs/02-local-development.md)
3. [Git and PR](docs/03-git-and-pr.md)
4. [CI quality gates](docs/04-ci.md)
5. [Release and deployment](docs/05-release-deployment.md)
6. [Database and recovery](docs/06-database-recovery.md)
7. [Security](docs/07-security.md)
8. [AI-assisted development](docs/08-ai-development.md)
9. [Adoption](docs/09-adoption.md)
10. [Operations](docs/10-operations.md)
11. [Testing and quality](docs/11-testing-and-quality.md)
12. [Observability, incident response, and data governance](docs/12-observability-and-data-governance.md)
13. [Enforcement mapping](docs/13-enforcement-mapping.md)

## Golden path
Issue in tracker of record → local branch → local checks → PR + review + CI → squash merge to main → immutable build → integration → staging/UAT → approval → production → monitor.

**Never edit source directly on production servers or deploy production from developer laptops.**

## Repository model
One repository per independently owned application; product repositories link to this handbook and implement stack-specific adapters. A monorepo is acceptable when it represents one independently owned product with clear workspace boundaries and CODEOWNERS. Once forked into GCG organization, designate that fork canonical.

## Product adapter
Each product repository MUST maintain a short adapter that names its issue tracker, runtime and test commands, environments, owners, required CI checks, and evidence locations. A root-level example is not enough: every independently runnable workspace MUST document its own `.env.example` and setup path. Deviations from MUST rules require an entry in the exception register.

## Templates and checklists
See [templates](templates/) and [checklists](checklists/). Samples are deliberately not ready-to-run production deployments.

- [Architecture decision record](templates/governance/adr.md)
- [Exception register](templates/governance/exception-register.md)
- [Incident checklist](checklists/incident.md)

## Adoption
Existing products are **not assumed compliant**. Inventory and reconcile live server state before migration. See [adoption checklist](checklists/repository-adoption.md).
