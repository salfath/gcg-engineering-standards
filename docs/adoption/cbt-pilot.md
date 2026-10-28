# CBT pilot: assessment and adoption proposal

**Status:** Proposed remediation plan; not certification or operational approval.
Assessment date: 2026-10-28. Handbook baseline:
`9a2c874853b778699fa433f2e0f72959ee0c8c7f`; CBT source baseline:
`0219bcd198e956e85ef8d8b2af98258641406796`.
The reviewed CBT workspace also contained uncommitted capacity-campaign work.
Source observations are scoped to that snapshot; live runtime was not audited.
Keep detailed evidence and topology in the product's restricted repository.

## Assessment observations

| Area | Observed evidence / limitation | Adoption action |
|---|---|---|
| Source identity | Checkout remote and deploy default name different source repositories | Confirm canonical source, build and release identity before automation |
| Main protection | GitHub branch API reported protected=false; ruleset API reported a hosting-plan limitation | Configure supported enforcement or approve a scoped expiring exception; verify with disposable PRs |
| CI execution | Workflows exist; Actions runs API returned total_count=0 at assessment time | Establish passing/failing run evidence; this result does not prove workflows never ran |
| Immutable release | Deploy installs Python dependencies and rebuilds frontend per tier; staging comparison uses tag name | Build once in CI; verify source SHA and exact artifact/manifest digests during promotion |
| Dependency inputs | Frontend has a lockfile; backend requirements use mostly lower bounds | Lock transitive Python dependencies and consume the lock during builds |
| Gate parity | Local full-QC script and CI cover different test groups; architecture check is not wired into those gates | Shared check scripts plus required aggregate status and explicit test matrix |
| Modularity | Architecture budget command returned five violations: two Vue files and three service functions | Resolve under reviewed product budgets and make the check mandatory |
| Recovery/monitoring | DR and observability documents describe targets/pending verification | Rehearse isolated whole-application recovery and alert routing; retain measured evidence |
| Runtime boundaries | Checked-in tier service definitions share one OS identity | Assess secret/file cross-tier access and resource limits; validate actual deployment separately |
| Rollback guidance | Manifest generator includes database downgrade guidance conflicting with product production constraints | Align on compatible application rollback; separately approve data recovery |

Evidence locations in CBT: `scripts/ops/deploy.sh`,
`scripts/ci/run_full_qc.sh`, `.github/workflows/`,
`backend/requirements.txt`, `scripts/ops/verify_architecture_budget.py`,
`scripts/ops/release_immutable_guards.sh`, `scripts/ops/services/`,
and development/release, DR and observability documentation.

Only the architecture budget command was executed during this assessment; it
failed. Application suites, deployment, PITR and real-device certification were
not executed. Reassess findings against the candidate before claiming closure.

## Phased acceptance

| Order | Proposed accountable role | Exit criterion |
|---|---|---|
| 1 — Governance | Engineering Lead + repository owner | Canonical repo and policy version approved; hosting supports enforcement or exception recorded; merge-block exercise passes |
| 2 — Development gates | CBT technical/CI owner | Clean-machine setup; Python lock; shared checks; meaningful required test groups; budget violations resolved |
| 3 — Immutable delivery | Release/platform owner | One CI build; manifest digests; exact-candidate UAT; approval/preflight rejects before mutation; staged and prod identities match |
| 4 — Operations | Platform/operations + incident authority | Isolated restore and compatible rollback drills; integrity/RPO/RTO measured; alerts reach named owner |
| 5 — Sustain | Product owner | Control/evidence review cadence and expiring exceptions; no direct runtime-source editing |

These are role assignments to confirm, not named owners or promised completion
dates. Product owners must create tracked tasks and attach evidence.

## Adapter starting point

CBT uses FastAPI/SQLAlchemy/Alembic, Vue/TypeScript, PostgreSQL, Redis/Celery and
platform-specific secure exam clients. A modular monolith is appropriate; this
proposal does not require a microservices or orchestration migration.

Existing development commands provide inputs for a future adapter:

- Setup: documented local dependency/database setup; add locked Python inputs.
- Dev: documented backend and frontend launch commands.
- Tests: integration, unit, contract, ops and frontend groups need an explicit matrix.
- Lint: include the existing architecture budget and selected format/static checks.
- Check: consolidate local/CI scripts; the existing full-QC name is not parity evidence.

Preserve CBT-specific requirements: Alembic-only runtime schema ownership;
explicit disposable-test guards; tenant/role boundaries; no automatic participant
deadline extension; configuration verification must not claim device attestation;
secure-client platform proof flags remain off until their device gates pass.
Shared-host isolation work never authorizes access to co-hosted product data or
services. Operational actions require product-authorized scope.

This plan supplies acceptance criteria, not a ready-to-run product adapter.
The implementation PRs belong in CBT after the handbook and product owners agree
on scope, migration windows and exception handling.
