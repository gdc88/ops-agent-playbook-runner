from ops_playbook_runner.models import Playbook
from ops_playbook_runner.report import render_report


def test_render_report_includes_privacy_note():
    report = render_report(Playbook("Demo", "Synthetic", "low", []), ["step OK"])
    assert "Synthetic demo only" in report
    assert "DRY RUN" in report
