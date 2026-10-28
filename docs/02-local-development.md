# Local development

Developers MUST write and test source locally. Server access is for approved operations only. Each repo MUST provide `.env.example`, a setup guide, and equivalent `setup`, `dev`, `test`, `lint`, `check` commands. Never commit secrets.

Each independently runnable application workspace MUST carry its own `.env.example` with safe placeholders and a one-line explanation for every required variable. A root-level example is not a substitute for a workspace that can be started on its own. Document supported operating systems and known limitations.

Prefer Docker Compose for databases, Redis and dependencies; app code MAY run natively for faster reload. Pin runtimes and use lockfiles. Use synthetic or anonymized seed data. Do not copy production dumps to personal devices without approved controls. Provide mocks or fixtures for external integrations so a clean machine can run the critical path without production credentials.

Suggested interface (must be implemented per product):
```bash
cp .env.example .env
make setup
make dev
make check
```

Document Linux/macOS/Windows support and mocks for integrations (SEB, RFID, CCTV, SATUSEHAT, etc.).
