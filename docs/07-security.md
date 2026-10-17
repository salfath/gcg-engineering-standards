# Security and privacy

MUST: never commit credentials; placeholders only in `.env.example`; use restricted production secret stores; least privilege; MFA for maintainers; secret/dependency scanning; HTTPS; audit logging for sensitive operations; vulnerability triage.

Untrusted PR workflows MUST NOT access production secrets. Rotate exposed credentials; history cleanup alone is insufficient. Production data in local environments requires explicit approval, minimization and anonymization. Sign/checksum distributable binaries where feasible. Document third-party keys and data flows.
