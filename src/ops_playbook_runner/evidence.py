from pathlib import Path
from datetime import datetime
import re


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "playbook"


def create_run_dir(playbook_name: str, base: str | Path = "runs") -> Path:
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = Path(base) / f"{stamp}-{slugify(playbook_name)}"
    path.mkdir(parents=True, exist_ok=True)
    return path
