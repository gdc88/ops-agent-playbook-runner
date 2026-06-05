from pathlib import Path
from ops_playbook_runner.loader import load_playbook


def test_load_example_playbook():
    playbook = load_playbook(Path("examples/playbooks/disk-space-triage.yaml"))
    assert playbook.name == "Disk Space Triage"
    assert len(playbook.steps) == 5
