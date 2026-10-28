# Git, branches and pull requests

Prefer trunk-based development with `main` as the integration branch. The
product adapter MUST name the protected integration branch for each repository.
An existing `develop` integration branch may be retained during adoption; a
branch rename is not a prerequisite for protecting changes or immutable delivery.
Use short-lived `feat/ISSUE-short-name`, `fix/ISSUE-short-name`,
`hotfix/ISSUE-short-name`, `docs/...`, `chore/...`. Prefer branches under
three days as a planning guideline, not a mandatory merge deadline. Split large
work; use feature flags where necessary. Prefer artifact promotion over
environment branches. Existing environment branches need a documented migration
plan; they MUST NOT bypass review, CI or identical-artifact promotion.

PRs MUST pass required CI and have at least one independent human approval.
Protect each integration branch against direct/force pushes and deletion; protect release tags
against replacement/deletion. Document narrowly scoped emergency bypass actors
and require incident evidence for their use. Prefer squash merge and branch
deletion. Conventional Commits recommended.

## Verify enforcement

Check plan/visibility support for private repositories before claiming protection.
Record sanitized configuration evidence and a disposable PR exercise showing
that missing approval or a failed required check prevents merge. Configuration
text in a runbook is not evidence of enforcement.

If enforcement is unavailable, record GCG-SCM-01 as GAP or an approved expiring
exception, identify the compensating release control, and resolve the hosting
capability before claiming compliance. Do not publish private source merely to
obtain a hosting feature.

Hotfixes follow PR, CI, new release, staging verification and controlled
production deployment. Emergency exceptions require an incident record,
authorized scope and retrospective; product integrity constraints still apply.
