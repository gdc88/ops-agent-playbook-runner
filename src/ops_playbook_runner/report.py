from .models import Playbook


def render_report(playbook: Playbook, events: list[str], dry_run: bool = True) -> str:
    lines = [
        f"# Playbook run report: {playbook.name}",
        "",
        f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}",
        "Safety policy: enabled",
        "",
        "## Steps",
        "",
    ]
    lines.extend(f"- {event}" for event in events)
    lines.extend(["", "Synthetic demo only. No real hosts or private data.", ""])
    return "\n".join(lines)
