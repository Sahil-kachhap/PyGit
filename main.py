import argparse
import json
from pathlib import Path
import sys


class Repository:
    def __init__(self, path="."):
        self.path = Path(path).resolve()
        self.git_dir = self.path / ".pygit"

        # .git objects
        self.objects_dir = self.git_dir / "objects"

        # ref objects
        self.ref_dir = self.git_dir / "refs"
        self.heads_dir = self.ref_dir / "heads"

        # HEAD FILE
        self.head_file = self.git_dir / "HEAD"

        # .git/index (Staging area)
        self.index_file = self.git_dir / "index"

    def init(self) -> bool:
        if self.git_dir.exists():
            return False
        self.git_dir.mkdir()
        self.objects_dir.mkdir()
        self.ref_dir.mkdir()
        self.heads_dir.mkdir()

        # create initial HEAD pointing to a branch
        self.head_file.write_text("ref: refs/heads/main\n")
        self.index_file.write_text(json.dumps({}, indent=2))

        print(f"Initialized Empty PyGit Repository in {self.git_dir}")

        return True


def main():
    parser = argparse.ArgumentParser(description="PyGit - A simple Git clone")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # Init Command
    init_parser = subparsers.add_parser("init", help="Initialize a Git Repository")
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "init":
            repo = Repository()
            if not repo.init():
                print("Repository already exists")
                return
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


main()
