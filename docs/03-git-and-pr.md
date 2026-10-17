# Git, branches and pull requests

Use trunk-based development: `main` is the only long-lived development branch. Use short-lived `feat/ISSUE-short-name`, `fix/ISSUE-short-name`, `hotfix/ISSUE-short-name`, `docs/...`, `chore/...`. Prefer branches under three days. Split large work; use feature flags where necessary. Do not create environment branches.

PRs MUST pass required CI and have at least one independent approval where enforcement is supported. No direct pushes, force pushes, deletion of main or self-approval. Prefer squash merge and branch deletion. Conventional Commits recommended. Protect release tags. Check GitHub plan and repo visibility before assuming ruleset enforcement.

Hotfixes follow PR, CI, new release, staging verification and controlled production deployment. Emergency exceptions require incident record and retrospective.
