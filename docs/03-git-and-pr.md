# Git, branches and pull requests

Use trunk-based development: `main` is the only long-lived development branch. Use short-lived `feat/ISSUE-short-name`, `fix/ISSUE-short-name`, `hotfix/ISSUE-short-name`, `docs/...`, `chore/...`. Prefer branches under three days and pull requests under roughly 400 changed lines. Split large work; use feature flags where necessary. Do not create environment branches.

The issue tracker may be Jira, GitHub Issues, Linear, or another approved system. The branch and pull request MUST include the tracker key (for example `PRX-123`) so intent and acceptance criteria are traceable.

## Staging and production promotion
`main` is the trunk, not a production branch. A release builds an immutable artifact from `main`, deploys that artifact to staging/UAT, and promotes the identical artifact to production after approval. Staging does not get a separate long-lived branch, and production is not built from a developer workstation.

## Monorepos
A monorepo is acceptable when the repository represents one independently owned product with clear workspace boundaries. Each workspace MUST have CODEOWNERS, its own setup commands, and an independent reviewer. If components have separate owners and release cadences, split the repository or document why the monorepo remains the safer option.

## Review and merge
PRs MUST pass required CI and have at least one independent approval where enforcement is supported. Security-sensitive changes (authentication, authorization, payments, clinical/exam data, privacy, migrations) SHOULD have a second domain-aware reviewer. No direct pushes, force pushes, deletion of main, or self-approval. Prefer squash merge and branch deletion. Conventional Commits recommended. Protect release tags. Check the platform plan and repository visibility before assuming ruleset enforcement.

If the platform cannot enforce a rule, record the exception and compensating control. A documented process is not a substitute for an enforceable check.

Hotfixes follow PR, CI, a new release, staging verification and controlled production deployment. Emergency exceptions require an incident record and retrospective.
