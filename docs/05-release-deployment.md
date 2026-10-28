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
source repository/SHA, CI evidence, artifact locations/digests, migration target,
previous-app schema compatibility evidence, supported clients, release notes
and rollback artifact. Link access-controlled evidence rather than embedding
secrets or participant data. Artifact identity and approvals may use separate
append-only records bound to the same manifest digest.

## Promotion

Local → optional integration/dev → staging/UAT → production.
Deployment MUST verify artifact integrity and provenance from an approved build
source, schema compatibility, staging approval for the exact digest, production
approval and product-specific preflight. Fail before mutation when these checks
fail. UAT must identify the tested candidate and outcomes.

CBT MUST prevent deployment during active exam windows using an operational gate
that prevents new admission racing the check. Salus/Akor require transaction and
data-integrity preflight. Implementations belong to product runbooks.

Use environment-scoped secrets and deployment locks. Stage to a new release
directory or equivalent and switch atomically after validation; preserve the
previous artifact. Never copy mutable shared downloads into a release without
binding their digests and compatibility.

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
