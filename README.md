# ops-agent-playbook-runner

Safe, auditable AI-assisted operations playbooks for local lab scenarios.

This repository demonstrates how infrastructure troubleshooting workflows can be made more repeatable with automation while keeping human approval, dry-run defaults, evidence capture, and privacy controls at the center.

It is a personal lab project, not a production incident platform. All examples use synthetic hosts, synthetic logs, and local demo data.

## Portfolio-safe visuals

These portfolio-safe visuals show the professional workflow without exposing private data, credentials, browser sessions, or personal records.

```mermaid
flowchart LR
    A[Playbook YAML] --> B[Schema validation]
    B --> C[Safety policy]
    C --> D[Dry-run executor]
    D --> E[Evidence bundle]
    E --> F[Markdown report]
```

## Why this exists

Infrastructure work is easier to trust when troubleshooting steps are repeatable, reviewed, and documented. This demo shows an AI-era operations pattern without connecting to real systems:

- playbooks define intended troubleshooting steps;
- dry-run mode is the default;
- risky commands are blocked by policy;
- manual approval steps are explicit;
- evidence and final reports are generated for review.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e . pytest pyyaml
python -m ops_playbook_runner run examples/playbooks/disk-space-triage.yaml --dry-run
pytest -q
```

Expected demo output:

```text
Playbook: Disk Space Triage
Mode: DRY RUN
Safety policy: enabled
Steps planned: 5
[1/5] check inventory: OK
[2/5] command df -h: dry-run recorded
[3/5] approval required: skipped in dry-run
[4/5] collect evidence: runs/.../evidence.md
[5/5] render report: runs/.../report.md
```

## Implemented features

- YAML playbook loading and validation.
- Dry-run execution by default.
- Safety policy for destructive command patterns.
- Manual approval step type.
- Evidence directory generation.
- Markdown report rendering.
- Unit tests for loader, safety, executor, and reports.

## Privacy, safety, and limitations

- Synthetic data only: no real Gmail, Telegram, LinkedIn, Google Sheets, CV, customer, or production infrastructure data.
- No secrets: `.env` files, tokens, browser profiles, cookies, and private Hermes configuration are intentionally excluded.
- No real remote execution: this MVP does not run SSH, WinRM, sudo, package installs, destructive filesystem changes, or network exfiltration.
- Human approval gates are modeled for review; in dry-run mode they are logged, not bypassed silently.
- This is a portfolio lab project, not a production incident-management platform.

See `docs/privacy-and-safety.md` for the publication checklist.

## Repository structure

```text
ops-agent-playbook-runner/
  README.md
  LICENSE
  pyproject.toml
  docs/
    architecture.md
    demo-walkthrough.md
    privacy-and-safety.md
    assets/
      architecture.svg
      cli-demo.txt
      sample-report.md
  examples/playbooks/disk-space-triage.yaml
  src/ops_playbook_runner/
  tests/
```

## Roadmap

- Add a small provider abstraction for optional local LLM summaries while keeping no-API mode default.
- Add more synthetic playbooks: certificate expiry and failed service triage.
- Add GitHub Actions after the repo is published.
- Add a sanitized GIF or asciinema recording after visual/privacy review.

## Hiring-positioning note

This project is designed to support a truthful portfolio message: experienced IT infrastructure professional building practical AI automation labs with safety, documentation, and evidence capture.
## Portfolio evolution

This repository is part of an evolving AI-automation portfolio, not a one-off demo. The projects show a growth path from job-search automation and local MVPs toward safer IT/cloud/security operations with agentic workflows.

Current portfolio map:

- **[Hermes SecOps Copilot](https://github.com/gdc88/boris-hermes-secops-portfolio)** — Newest portfolio layer: Hermes/OpenClaw-style AI automation for cloud security operations, M365/Azure readiness, Copilot governance, and agentic workflows. Live page: https://gdc88.github.io/boris-hermes-secops-portfolio/
- **[AI Automation Ops Lab](https://github.com/gdc88/boris-ai-automation-ops-lab)** — Operational base layer: self-hosted AI automation patterns, Telegram delivery, scheduled agents, browser-assisted workflows, and infrastructure operations thinking.
- **[Ops Agent Playbook Runner](https://github.com/gdc88/ops-agent-playbook-runner)** — Engineering proof layer: safe, auditable, dry-run-first operations playbooks with evidence bundles and policy controls.
- **[AI Resume Adapter Bot](https://github.com/gdc88/ai-resume-adapter-bot)** — Career automation layer: ATS/job-description analysis and truthful resume tailoring workflow for the German market.
- **[JobMatch AI](https://github.com/gdc88/JobMatch-AI)** — Course/final-project layer: static MVP for job-match analysis, recruiter message drafting, and portfolio demonstration.

Growth direction:

- Keep public repositories sanitized and recruiter-safe.
- Prefer clear architecture, safety boundaries, screenshots/visuals, and evidence over private operational data.
- Update each project as the overall system matures: better runbooks, stronger guardrails, clearer German-market positioning, and more polished demos.
- Use GitHub as the proof layer and LinkedIn as the recruiter funnel once the LinkedIn profile is aligned with the same positioning.
