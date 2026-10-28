# Release and deployment

**Build once; promote the identical immutable artifact.** Default release tag:
`vYYYY.MM.DD-N` (CalVer). A protected tag labels a release; it does not replace
the full source SHA and artifact digest.

## Build and manifest

Build from clean reviewed source in CI using locked dependencies. Container-capable
apps SHOULD publish digest-addressed images; other apps MAY publish release
bundles with all runtime dependencies prepared for the target platform.
Staging/prod MUST NOT rebuild source or resolve/install dependencies during deploy.

The [manifest](../templates/project/release-manifest.example.yml) MUST bind
each component source repository/SHA, reviewed dependency/platform identities,
CI evidence, artifact locations/digests, migration target,
previous-app schema compatibility evidence, supported clients, release notes
and rollback artifact. Link access-controlled evidence rather than embedding
secrets or participant data. Artifact identity and approvals may use separate
append-only records bound to the same manifest digest.

## Promotion

Local workspace → reviewed `main` → dev → staging/UAT → production.
The promotable build is created once from an exact `main` revision (or reviewed
component revisions on their respective `main` branches). A PR validation build
is not automatically a release artifact. Dev may advance while staging/production
retain an earlier candidate; promotion always selects an explicit manifest digest.
Deployment MUST verify artifact integrity and provenance from an approved build
source, schema compatibility, staging approval for the exact digest, production
approval and product-specific preflight. Fail before mutation when these checks
fail. UAT must identify the tested candidate and outcomes.

Adapters MUST define critical-session, transaction and data-integrity preflight
for their risk profile. Where active work blocks deployment, a lock or admission
gate must prevent new work racing the check. Implementations and maintenance
windows belong to product runbooks.

Use protected staging/production environments or equivalent enforced approval
controls, environment-scoped secrets and least-privilege deployment identities.
Verify an approved SSH host key when SSH is used; never disable verification.
Use per-target deployment locks and non-cancelling concurrency: a newer commit
MUST NOT automatically cancel an active production activation or migration.
Provide an authorized controlled-abort procedure; non-cancelling does not mean
uninterruptible after operator assessment. Stage to a new release
directory or equivalent and switch atomically after validation; preserve the
previous artifact. Never copy mutable shared downloads into a release without
binding their digests and compatibility.

Environment configuration is injected separately without rebuilding or modifying
artifact bytes; version configuration references and validate compatibility without
placing secret values in manifests. Stage-required approval, UAT, production
approval and smoke checks fail closed; missing or skipped evidence is not PASS.

Record PR, SHA, digests, migration result, approvers, actor, timestamps and
success/failure. Run smoke checks and monitor; never mark a failed deployment
current merely because checkout succeeded.

## Rollback and clients

Rollback MUST redeploy an earlier validated artifact compatible with the current
schema. Do not automatically downgrade or restore the production database.
Incompatible data recovery requires separate incident approval, reconciliation
and an explicit assessment of writes that could be lost.

APK/desktop installers need separate versioned digests, signatures where supported,
backend compatibility and revocation policy. Client artifacts need not share the
backend version but their supported combinations must be recorded.

Reference: [SLSA provenance and supply-chain model](https://slsa.dev/spec/v1.2/).
This handbook does not claim a SLSA level.
