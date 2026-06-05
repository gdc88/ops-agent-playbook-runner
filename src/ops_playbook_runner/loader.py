from pathlib import Path
import yaml
from .models import Playbook, validate_playbook


def load_playbook(path: str | Path) -> Playbook:
    data = yaml.safe_load(Path(path).read_text())
    if not isinstance(data, dict):
        raise ValueError("Playbook YAML must be a mapping")
    return validate_playbook(data)
