#!/usr/bin/env python
#
# A simple linter that validates all markdown files in the repository.

import subprocess
import sys
from pathlib import Path


def main():
    """Main function."""
    root = Path(__file__).parent
    files_to_check = []
    for doc_type in ["policies", "standards", "processes", "guidance"]:
        files_to_check.extend(list(root.glob(f"{doc_type}/*.md")))

    if not files_to_check:
        print("No markdown files found to check.")
        return

    cmd = [sys.executable, str(root / "validate.py")] + files_to_check
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("Linter failed with the following errors:")
        print(result.stderr)
        sys.exit(1)
    else:
        print("Linter passed.")


if __name__ == "__main__":
    main()
