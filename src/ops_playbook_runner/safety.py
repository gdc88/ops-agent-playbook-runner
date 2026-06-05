import re

DANGEROUS_PATTERNS = [
    r"\brm\s+-rf\b",
    r"\bsudo\b",
    r"/etc/passwd",
    r"/etc/shadow",
    r"\bcurl\b.*\|\s*sh",
    r"\bwget\b.*\|\s*sh",
    r"\bmkfs\b",
    r"\bdd\s+if=",
    r"\bshutdown\b",
    r"\breboot\b",
]


def is_command_allowed(command: str) -> bool:
    return not any(re.search(pattern, command, re.IGNORECASE) for pattern in DANGEROUS_PATTERNS)


def explain_command_policy(command: str) -> str:
    if is_command_allowed(command):
        return "allowed for dry-run recording"
    return "blocked by safety policy"
