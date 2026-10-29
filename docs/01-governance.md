# Governance and policy levels

- **MUST**: mandatory for the approved version and applicable product scope,
  unless Engineering Lead approves a documented, time-limited exception.
- **SHOULD**: default recommendation; deviations need rationale in an ADR.
- **MAY**: team choice.

Version 0.2.0 is ratified by the owner, effective 2026-10-29, for normative baseline
`bdc6b79a53730ba6f67bc88a2a5500992a8d579f`; see the
[ratification record](../.github/policy-ratification.json). Future policy versions
require approval of an exact version/commit and effective date. Existing products
may adopt immediately: a calendar transition window is optional and never a blanket
waiver. Application cutover still requires the applicable regression, independent
review, immutable identity, recovery and authorization gates. No absolute absence
of regressions can be promised by documentation or tests. A policy merge does not
certify a product or approve a production deployment.

## Ownership and document hierarchy

Each repo MUST identify its technical owner, independent reviewer, deployment
owner, incident contact and deputy, runtime stack, canonical repository,
environments and data classification. Roles must resolve to accountable people
or maintained team contacts in a restricted directory where necessary.

Authority flows from approved GCG policy → versioned product adapter →
product ADRs/runbooks → agent instructions. Product documents may add stricter
safety controls. They cannot silently weaken a global MUST. Conflicts require
an explicit policy change or approved exception; unresolved conflicts block the
affected adoption/release gate.

Products MUST pin their adopted handbook version or full commit, record local
adapter paths and applicable controls, and adopt changes through reviewed PRs.
Do not automatically follow a moving handbook branch.

The same approved baseline applies to all current and future GCG applications.
Adapters record applicability and implementation, not product-specific alternate
standards. Product assessments and operational evidence belong outside this
universal handbook.

## Controls and exceptions

The [control register](12-control-register.md) supplies IDs, minimum evidence and
verification ownership. Each adapter MUST map applicable controls to commands,
configuration, people and evidence. Use PASS, GAP, EXCEPTION, NOT_APPLICABLE or
NOT_ASSESSED; NOT_APPLICABLE needs reviewed rationale.

An exception MUST name the control, product/scope, risk, compensating controls,
owner, Engineering Lead approval, expiry and remediation issue. Expiry without
renewal or remediation is a GAP, not implicit approval. Store no secrets or
personal incident details in public evidence.

## Minimum Definition of Done

Tracked issue (Jira or equivalent); acceptance criteria met; relevant tests and
security/privacy assessment; documentation updated; CI green on the reviewed
commit; independent review; compatibility and release/rollback impact recorded.
Documentation-only changes may use document validation with rationale; tests
must verify meaningful behavior rather than merely repeat the implementation.

Prioritize safety and correctness over tool uniformity. Infrastructure choices
and numerical code-size budgets belong in product adapters.
