# GCG Engineering Standards

**Status:** Draft v0.1.0 — pending GCG Engineering Lead approval.
Unreleased proposals are not approved policy.
**Scope:** Scola, Salus, CBT, Akor, Prima, and future GCG products.

This is the technology-neutral engineering handbook. **MUST** = mandatory once
the applicable version is approved and adopted; **SHOULD** = recommended unless
a deviation is documented; **MAY** = optional. Existing products are not assumed
compliant. Record the adopted version, gaps, owners and evidence.

## Start here

1. [Governance and document hierarchy](docs/01-governance.md)
2. [Local development](docs/02-local-development.md)
3. [Git and PR](docs/03-git-and-pr.md)
4. [CI quality gates](docs/04-ci.md)
5. [Release and deployment](docs/05-release-deployment.md)
6. [Database and recovery](docs/06-database-recovery.md)
7. [Security](docs/07-security.md)
8. [AI-assisted development](docs/08-ai-development.md)
9. [Adoption](docs/09-adoption.md)
10. [Operations](docs/10-operations.md)
11. [Application engineering](docs/11-application-engineering.md)
12. [Verifiable control register](docs/12-control-register.md)

## Golden path

Tracked issue → acceptance criteria → local branch and checks → PR + independent
review + CI → merge to protected integration branch → immutable build → staging/UAT → recorded
approval → production promotion of the same digest → monitor.

**Never edit source directly on production servers or deploy production from
developer laptops.** Approved operations run through the product deployment path.

## Repository model

Repository boundaries follow ownership and independently releasable components.
A product MAY use separate frontend/backend repositories or a monorepo; its
adapter MUST identify component owners, shared platform dependencies and how
compatible component revisions are bound into one release. Each product identifies its
canonical source, build and release repositories; a fork does not silently become
canonical. Product adapters implement this handbook for their stack without
weakening product safety invariants.

## Use and verification

- Start with the [adoption checklist](checklists/repository-adoption.md).
- Copy the [product adapter template](templates/project/engineering-adapter.md)
  and [adoption record](templates/project/standards-adoption.example.yml).
- Use the [release checklist](checklists/release.md) and
  [manifest example](templates/project/release-manifest.example.yml).
- Record any mandatory-control exception using the
  [exception template](templates/project/exception.md).
- See the [CBT pilot proposal](docs/adoption/cbt-pilot.md) for concrete gaps and
  acceptance gates. It is not a product certification.
- See the [Scola adoption proposal](docs/adoption/scola.md) for the Vue/Odoo
  adapter boundary, source-assessed gaps and phased acceptance gates.

Samples are deliberately not ready-to-run production deployments. Placeholder
commands must fail. Run `python3 scripts/check_handbook.py` to check local links.
