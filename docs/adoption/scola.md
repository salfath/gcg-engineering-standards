# Scola: source assessment and adoption proposal

**Status:** Proposed; not an approved adapter, certification or deployment authority.
Assessment date: 2026-10-28. Approved policy version: not yet assigned.
Assessed handbook baseline: `9a2c874853b778699fa433f2e0f72959ee0c8c7f`.
Scola frontend baseline: `ab76ccfa7d726305d1a915fb605195acf6950400`,
branch `develop`, clean worktree at assessment time.

The assessment inspected frontend documentation, package/configuration files and
workflows, plus a limited backend capability-registry sample. Backend HEAD and
full backend behavior were not audited. No application tests, GitHub protection
checks, runtime probes, deployment or recovery drills were executed. Findings
are source/configuration observations, not evidence of production compliance.
Keep hostnames, tenant identities, credentials and operational evidence restricted.

## Adapter boundary and preserved controls

Scola uses Vue/Vite and custom Odoo modules in separate repositories. Retain that
boundary and separate commits/PRs. The product adapter should link to the existing
`docs/ai-guidelines/HANDBOOK.md`, API/coding/security guidance and release contract;
do not copy their command lists into this global handbook. Pin the approved GCG
version and record conflicts and migration decisions in the product adapter.

Preserve same-origin product APIs, backend authorization as the final authority,
tenant/company scope, capability checks and negative authorization tests.
Preserve frontend size budgets and documentation governance. Frontend visibility
is a UX control, not an authorization boundary.

Preserve exact paired FE/BE candidates, immutable demo/UAT/production releases,
explicit production authorization, named-tenant promotion, canary observation and
stop-on-first-failure. These are existing product safety requirements, not proof
that every workflow enforces them. Runtime identity and certification must be
verified separately from source or unit-test results.

## Source-assessed gaps

GAP below describes an observed mismatch against the proposed controls. It does
not assert that an approved policy was already violated. Mixed findings must be
split into separately evidenced items in the product adoption register.

| Control / status | Observed evidence | Required adoption action |
|---|---|---|
| GCG-GOV-01 / NOT_ASSESSED | Product Handbook and specialist precedence exist; global adoption and named accountable contacts were not verified | Pin approved policy; link maintained owners and adapter; explicitly reconcile precedence |
| GCG-SCM-01 / NOT_ASSESSED | FE guidance uses `develop`, BE guidance uses `main`; no frontend CODEOWNERS file found | Name protected integration branches; verify actual protection, independent review and required-check enforcement; CODEOWNERS absence alone is not proof of missing review |
| GCG-CI-01 / GAP | Product guidance permits server-first `[skip ci]` after local QC; browser smoke is optional and swallows failures | Require reviewed-SHA CI evidence; remove routine bypass or record a scoped expiring exception; make required release smoke fail closed |
| GCG-CI-02 / GAP | Workflow actions use version tags; permissions are not explicit; deployment disables SSH host-key checking | Pin audited action SHAs, declare minimal permissions and verify a pre-approved host key; separate validation from deployment credentials |
| GCG-DEV-01 / GAP | Setup guide recommends Node 20/22; CI selects 24; FE/BE parity checkout tracks BE `main` | Select and validate one supported runtime baseline; record exact BE SHA used for checks and releases |
| GCG-DEV-02 / GAP | npm commands exist but Makefile exposes QA commands rather than the documented setup/dev/test/lint/check interface | Publish equivalent command mappings and a shared check entry point; distinguish developer, shared integration and disposable test targets |
| GCG-ENG-02 / GAP | `type-check` includes Playwright/E2E TypeScript with `strict: false`, not application Vue source | State current coverage honestly; add application-aware type validation with a reviewed incremental baseline |
| GCG-REL-01 / GAP | Build and deploy jobs each install dependencies and build FE | Build once; verify frontend artifact, retain checksum/provenance, and deploy that output without rebuilding |
| GCG-REL-02 / GAP | Staging workflow rsyncs the demo docroot while product contract requires immutable demo releases | Consolidate demo promotion through immutable tooling; verify resolved runtime binding before assessing actual impact |
| GCG-SEC-02 / NOT_ASSESSED | Reviewed frontend workflows contain no dedicated dependency/secret-scanning steps; organization controls were not inspected | Verify external scanning coverage or add checks, triage policy and expiry-based exceptions; do not expose tracked environment values in evidence |
| GCG-DB-01, GCG-DR-01, GCG-OPS-01/02 / NOT_ASSESSED | Product release contract covers module upgrades, identity, isolation and rollback; live execution was not assessed | Obtain isolated migration/restore/rollback and alert evidence, measured recovery objectives and shared-host residual assessment |

Evidence entry points in the frontend repository:
`docs/ai-guidelines/HANDBOOK.md`,
`docs/ai-guidelines/release-environment-promotion.md`,
`docs/operations/runbooks/environment-isolation-and-promotion.md`,
`docs/ai-guidelines/local-dev-setup.md`, `.github/workflows/deploy-unified.yml`,
`.github/workflows/promote-uat.yml`, `.github/pull_request_template.md`,
`package.json`, `Makefile`, and `tsconfig.typecheck.json`.
The PR template also contains historical menu/RBAC milestones; replace them with
change-specific tests, privacy/security, API/database compatibility and rollback
impact. Reassess all findings against the implementation candidate.

## Phased acceptance and ownership

| Order | Proposed accountable role | Exit criterion |
|---|---|---|
| 1 — Governance | Engineering Lead + Scola technical owner | Approved policy ref; component/owner map; each control mapped to evidence or gap; branch and CI-bypass decisions recorded without silently overriding current product instructions |
| 2 — Developer and PR gates | Scola CI owner | Clean-checkout setup works; runtime and command mappings agree; failed checks and missing approval block a disposable PR; scans and risk-selected tests run on reviewed source refs |
| 3 — Immutable delivery | Scola release/platform owner | One verified FE output with paired BE/platform identities; demo uses immutable tooling; digest mismatch, absent approval and failed/skipped required smoke block promotion; activation and rollback tested in disposable targets |
| 4 — Product safety and recovery | Backend/security + operations owners | Tenant/role negative tests, retry/concurrency tests for affected critical mutations, disposable Odoo install/upgrade with explicit module list and single migrator, compatible app rollback and isolated DB/filestore restore drills pass; recovery objectives and alert routing measured |
| 5 — Sustain | Scola technical owner | Owners, remediation issues, review cadence, evidence retention and expiring exceptions maintained; source, runtime and certification claims remain separate |

Roles and scheduling require product-owner confirmation. This proposal assigns
no named people, deadlines or production permissions. An unknown result remains
NOT_ASSESSED; a partial implementation remains GAP with the observed coverage
recorded, rather than PASS. Detailed evidence belongs in restricted CI artifacts
or the product's approved evidence store, not public documentation dumps.

## First implementation slice

Use one bounded product change to exercise the whole path: tracked acceptance
criteria, reviewed FE/BE revisions, required checks, one artifact build, exact
candidate UAT, negative tenant probe where applicable and controlled promotion.
Accept it only when provenance connects PR, checks, artifact and observed runtime.
A branch rename or infrastructure rewrite is not required for this slice.
Any existing mandatory product instruction stays in force until changed through
its authorized governance process; this handbook proposal does not override it.
