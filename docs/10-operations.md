# Operations, observability and ownership

Each production application MUST identify technical/deployment owners and
deputies, incident contacts, runbook, severity/escalation policy, central logs,
alerts and post-incident review. Maintain contact details in an access-controlled
directory when a public repository is unsuitable.

Distinguish process liveness, dependency readiness and operational integrity.
Define service objectives, alert thresholds/windows, destinations and actionable
runbooks. Verify alert injection → receipt by owner → safe action → recovery.
A configuration file alone does not establish that monitoring operates.

Production changes MUST trace to PR, full SHA, artifact/manifest digests,
approvers, deployment result and smoke/observation outcomes. Retain failure
records too. Logs must redact credentials and sensitive content; diagnostic
evidence needs access and retention controls.

On shared servers, assess Unix identities, secret/file permissions, network
access, storage and CPU/memory/IO quotas. Separate ports/databases alone do not
establish isolation. Where shared identities remain, document the cross-tier
access risk and compensating controls; stronger isolation is prioritized by risk.

Measure lead time, deployment frequency, change failure rate and recovery time
without sacrificing safety. Review controls after material topology/security
changes and on an owner-approved cadence; expire stale evidence and exceptions.

## Service objectives and incidents

Define SLIs/SLOs and an error-budget response for critical user journeys, with
latency/error/saturation and dependency metrics appropriate to the service.
Structured logs include timestamp, severity, service/environment, outcome and
request/trace correlation where applicable. Test redaction of secrets embedded
in formatted messages, not only named fields. Claimed error tracking or APM must
be initialized and validated; a feature flag alone proves nothing.

Liveness detects an unrecoverable process condition; readiness indicates ability
to serve traffic with required dependencies. Do not make a temporary dependency
outage cause fleet-wide liveness restarts. Platform-native signals may replace
HTTP endpoints when the adapter documents equivalent semantics.

Maintain a severity matrix, response/communication targets, primary/backup
escalation routes, incident channel and customer communication method. Major
incidents require a blameless review with owned actions and due dates. Use the
[incident checklist](../checklists/incident.md). Evidence retention and collection
must respect [data governance](14-data-governance.md).
