# Data governance

Each adapter MUST define data ownership and handling requirements appropriate to
its risk profile. Apply these to services, analytics, logs, exports, backups,
fixtures, AI tools and third parties, not only primary databases.

## Inventory and privacy assessment

Classify data as public, internal, confidential or restricted with handling rules.
Credentials and sensitive identity, health, financial and session records default
to restricted unless a reviewed assessment establishes a different treatment.
Maintain an inventory of purpose, collection basis, location, recipients, access,
retention and accountable owner. Minimize collected fields; aggregate or
pseudonymize when identifiers are unnecessary.

High-risk personal-data processing or a new purpose MUST receive a documented
privacy impact assessment or equivalent review before launch. The designated
privacy/legal owner determines applicable obligations, transfer restrictions and
breach-notification requirements; this handbook is not legal advice or a fixed
jurisdiction-specific compliance checklist.

## Lifecycle and external processing

Define retention, deletion, legal hold and propagation through caches, files,
exports, backups and downstream systems. Document how restores reapply deletion
or hold decisions. Backups inherit source classification. Restrict access to
sensitive evidence and audit meaningful access/administrative actions.

Maintain vendor/subprocessor records, approved purposes and access, transfer
locations and incident contacts. Review new third-party data flows before use.
Agents and diagnostic tools follow the same disclosure restrictions as humans.
Link the private disclosure/escalation route from the security profile.
