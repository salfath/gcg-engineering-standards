# Enforcement mapping

A rule is not a standard until it is enforced or explicitly excepted. This document maps MUST rules to enforceable controls.

## Source control platform

- **MUST** protect the default branch and release branches with a ruleset or branch protection: no direct push, no force push, no deletion.
- **MUST** require a pull request, at least one independent approval, CODEOWNERS review for owned paths, and resolution of review threads.
- **MUST** require the CI checks named in the repository adapter. A red check blocks merge.
- **MUST** dismiss stale approvals after new commits and prevent self-approval.
- **SHOULD** require signed commits or signed release tags where the platform supports it.

## Environments and secrets

- **MUST** model staging and production as protected environments with required reviewers, environment-scoped secrets, and a deployment branch or tag policy.
- **MUST NOT** expose production secrets to pull-request workflows or untrusted code.
- **MUST** use least-privilege deployment identities. Shared administrator SSH accounts are not acceptable for routine deployment.
- **SHOULD** use short-lived credentials or OIDC federation where the platform and target support it.

## CI required checks baseline

The product adapter MUST name the real commands for:

- lint and format check;
- unit and integration tests;
- build;
- secret scanning;
- dependency vulnerability audit;
- static application security testing;
- database migration validation;
- API contract or OpenAPI drift check;
- coverage reporting;
- immutable artifact build.

## Release evidence

Every production release MUST retain: pull request and issue link, commit SHA, artifact digest, schema revision, test and UAT evidence, approvals, deployment result, and rollback target.

## Exceptions

If the platform plan cannot enforce a MUST (for example, private-repository branch protection unavailable), the product MUST:

1. record the gap in the exception register;
2. name an accountable owner and compensating control;
3. set an expiry date and review date;
4. avoid claiming compliance until the control is enforced.

## Evidence retention

Define where evidence is stored, who can access it, and how long it is retained. Keep it at least for the supported lifetime of the release and any legal or audit requirement.
