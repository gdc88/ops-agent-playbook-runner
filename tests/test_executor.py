from pathlib import Path
from ops_playbook_runner.loader import load_playbook
from ops_playbook_runner.executor import execute


def test_execute_dry_run_creates_report(tmp_path):
    playbook = load_playbook(Path("examples/playbooks/disk-space-triage.yaml"))
    events, run_dir = execute(playbook, runs_dir=tmp_path)
    assert len(events) == 5
    assert (run_dir / "report.md").exists()
    assert "dry-run recorded" in "\n".join(events)
