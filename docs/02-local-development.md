# Local development

Developers MUST write and test source in development workspaces. Runtime servers
are for approved operations. Each repo MUST provide `.env.example`, clean-machine
setup instructions and equivalent `setup`, `dev`, `test`, `lint`, `check`
commands. Never commit secrets.

Prefer Docker Compose for databases, Redis and dependencies; app code MAY run
natively for faster reload. Pin supported runtime versions and lock direct and
transitive dependencies. CI/release builds MUST use the reviewed dependency lock;
lock updates go through PR and vulnerability review. Document platform-specific
constraints and unsupported environments.

Use synthetic seed data. Anonymization must be verified before data is treated
as safe. Production dumps require separately approved controls.

## Command contract

| Command | Required behavior |
|---|---|
| setup | Install locked dependencies and initialize a disposable local environment |
| dev | Start the documented local app and dependencies, with explicit endpoints |
| test | Run the test groups declared by the adapter |
| lint | Check formatting, static rules and applicable architecture budgets |
| check | Run the mandatory local equivalent of the PR gate |

Commands MUST propagate failures. Placeholder adapters MUST exit nonzero.
`check` and CI must use the same scripts/configuration; document CI-only
browser, device or external-service checks. A skipped check is not a pass.

Document Linux/macOS/Windows support and integration mocks (SEB, RFID, CCTV,
SATUSEHAT, etc.). Real-device and recovery certification remain separate gates.
