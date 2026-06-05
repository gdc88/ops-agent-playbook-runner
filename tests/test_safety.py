from ops_playbook_runner.safety import is_command_allowed, explain_command_policy


def test_allows_harmless_read_only_command():
    assert is_command_allowed("df -h")
    assert "allowed" in explain_command_policy("df -h")


def test_blocks_destructive_command():
    assert not is_command_allowed("sudo rm -rf /")
    assert "blocked" in explain_command_policy("sudo rm -rf /")
