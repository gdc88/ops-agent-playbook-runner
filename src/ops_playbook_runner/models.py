from dataclasses import dataclass
from typing import Any

ALLOWED_STEP_TYPES = {"check", "command", "approval", "collect", "note"}

@dataclass(frozen=True)
class Step:
    type: str
    name: str
    details: str = ""
    command: str = ""
    prompt: str = ""

@dataclass(frozen=True)
class Playbook:
    name: str
    description: str
    risk_level: str
    steps: list[Step]


def validate_playbook(data: dict[str, Any]) -> Playbook:
    for field in ["name", "description", "risk_level", "steps"]:
        if field not in data:
            raise ValueError(f"Missing required playbook field: {field}")
    if not isinstance(data["steps"], list) or not data["steps"]:
        raise ValueError("Playbook must include at least one step")
    steps: list[Step] = []
    for raw in data["steps"]:
        step_type = raw.get("type")
        if step_type not in ALLOWED_STEP_TYPES:
            raise ValueError(f"Unsupported step type: {step_type}")
        if not raw.get("name"):
            raise ValueError("Every step needs a name")
        if step_type == "command" and not raw.get("command"):
            raise ValueError("Command steps need a command")
        steps.append(Step(type=step_type, name=raw["name"], details=raw.get("details", ""), command=raw.get("command", ""), prompt=raw.get("prompt", "")))
    return Playbook(name=data["name"], description=data["description"], risk_level=data["risk_level"], steps=steps)
