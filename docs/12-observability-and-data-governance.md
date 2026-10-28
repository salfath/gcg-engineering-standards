# Observability, incident response, and data governance

Production safety depends on knowing what the system is doing and protecting the data it holds.

## Observability

- **MUST** expose liveness and readiness endpoints that reflect the dependencies required to serve traffic.
- **MUST** emit structured logs with request or trace identifiers, timestamp, severity, service, environment, and outcome. Do not log secrets, tokens, credentials, or unmasked PII.
- **MUST** test log redaction. Path-based redaction alone does not remove secrets embedded in formatted messages.
- **MUST** collect metrics for latency, error rate, saturation, queue depth, and dependency health.
- **MUST** define SLIs and SLOs for critical user journeys, with error budgets and alerts tied to an owner and runbook.
- **SHOULD** centralize logs with retention, access control, and a documented retention period.
- **SHOULD** use tracing across service boundaries where multiple components participate in one request.
- If error tracking or APM is claimed as supported, **MUST** prove it is initialized, tested, and redacts sensitive data. A feature flag or commented integration is not evidence.

## Incident response

- **MUST** maintain a severity matrix with examples, response targets, communication cadence, and an accountable incident owner.
- **MUST** name a primary and secondary on-call route, escalation path, incident channel, and status communication method.
- **MUST** preserve minimal evidence without copying PII or secrets into tickets.
- **MUST** hold a blameless post-incident review for P0/P1 incidents, with action items, owners, and due dates.
- **SHOULD** publish a status page or customer communication template for user-facing incidents.

## Data governance

- **MUST** classify data as public, internal, confidential, or restricted. Identity, health, financial, exam, and authentication data are restricted unless a reviewed decision says otherwise.
- **MUST** maintain a data inventory covering purpose, lawful basis, retention, location, access, and third-party recipients.
- **MUST** complete a DPIA or equivalent privacy review before processing high-risk personal data or launching a new purpose.
- **MUST** define retention, deletion, legal hold, and backup treatment. Backups inherit the classification of their source data.
- **MUST** maintain a vendor and subprocessor register and review cross-border transfer and incident obligations.
- **MUST** follow applicable breach-notification law and regulation (for example Indonesia's UU PDP No. 27/2022 where applicable).
- **SHOULD** minimize collected fields and pseudonymize or aggregate where the product does not need identifiers.
