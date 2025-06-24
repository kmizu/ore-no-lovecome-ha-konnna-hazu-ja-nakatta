#!/usr/bin/env python3
"""Build script for the MkDocs site."""

import subprocess
import sys


def main():
    """Build the MkDocs site."""
    try:
        print("Building MkDocs site...")
        subprocess.run([sys.executable, "-m", "mkdocs", "build"], check=True)
        print("Build complete! Site generated in 'site' directory.")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()