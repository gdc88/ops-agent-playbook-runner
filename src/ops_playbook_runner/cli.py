import argparse
from .loader import load_playbook
from .executor import execute


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ops-playbook-runner")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("playbook")
    run.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args(argv)
    playbook = load_playbook(args.playbook)
    events, run_dir = execute(playbook, dry_run=args.dry_run)
    print(f"Playbook: {playbook.name}")
    print("Mode: DRY RUN")
    print("Safety policy: enabled")
    print(f"Steps planned: {len(playbook.steps)}")
    for event in events:
        print(event)
    print(f"Report: {run_dir / 'report.md'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
