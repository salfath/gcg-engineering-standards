# Operations, observability and ownership

Each production application MUST identify technical/deployment owners, runbook, health checks, central logs, alerts, incident severity policy and post-incident review. Production changes MUST trace to PR, commit, artifact digest, approver and deployment result. Measure lead time, deployment frequency, change failure rate and recovery time without sacrificing safety.

## Observability
MUST define SLIs and SLOs for critical user journeys, with error budgets, dashboards, and alerts tied to an owner and runbook. MUST use structured logs with request/trace identifiers and tested PII redaction. SHOULD centralize logs with documented retention and access control. Health checks MUST reflect the dependencies required to serve traffic.

## Incidents and on-call
MUST maintain a severity matrix, primary/secondary on-call route, escalation path, incident channel, and communication cadence. P0/P1 incidents require a blameless post-incident review with owned action items and due dates. Preserve evidence without copying PII or secrets.

## Shared infrastructure
On shared servers, isolate Unix users, permissions, network access, storage and resource quotas. Separate ports/databases alone are not infrastructure isolation; prioritize stronger isolation for critical workloads. Deployment identities MUST be least privilege and MUST NOT share routine administrator access.
