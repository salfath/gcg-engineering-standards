# Local development

Developers MUST write and test source locally. Server access is for approved operations only. Each repo MUST provide `.env.example`, setup guide and equivalent `setup`, `dev`, `test`, `lint`, `check` commands. Never commit secrets.

Prefer Docker Compose for databases, Redis and dependencies; app code MAY run natively for faster reload. Pin runtimes and use lockfiles. Use synthetic/anonymized seed data. Do not copy production dumps to personal devices without approved controls.

Suggested interface (must be implemented per product):
```bash
cp .env.example .env
make setup
make dev
make check
```

Document Linux/macOS/Windows support and mocks for integrations (SEB, RFID, CCTV, SATUSEHAT, etc.).
