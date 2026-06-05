from pathlib import Path
from .models import Playbook
from .safety import is_command_allowed
from .evidence import create_run_dir
from .report import render_report


def execute(playbook: Playbook, dry_run: bool = True, runs_dir: str | Path = "runs") -> tuple[list[str], Path]:
    events: list[str] = []
    run_dir = create_run_dir(playbook.name, runs_dir)
    for index, step in enumerate(playbook.steps, start=1):
        prefix = f"[{index}/{len(playbook.steps)}] {step.type} {step.name}:"
        if step.type == "command":
            if not is_command_allowed(step.command):
                events.append(f"{prefix} blocked by safety policy")
            else:
                events.append(f"{prefix} dry-run recorded command `{step.command}`" if dry_run else f"{prefix} execution disabled in MVP")
        elif step.type == "approval":
            events.append(f"{prefix} approval required; skipped in dry-run")
        elif step.type == "collect":
            events.append(f"{prefix} evidence.md")
        else:
            events.append(f"{prefix} OK")
    report = render_report(playbook, events, dry_run=dry_run)
    (run_dir / "report.md").write_text(report)
    return events, run_dir
