# Operations, observability and ownership

Each production application MUST identify technical/deployment owners, runbook, health checks, central logs, alerts, incident severity policy and post-incident review. Production changes MUST trace to PR, commit, artifact digest, approver and deployment result. Measure lead time, deployment frequency, change failure rate and recovery time without sacrificing safety.

On shared servers, isolate Unix users, permissions, network access, storage and resource quotas. Separate ports/databases alone are not infrastructure isolation; prioritize stronger isolation for critical workloads.
