#!/usr/bin/env python3
"""Serve script for the MkDocs site."""

import subprocess
import sys


def main():
    """Serve the MkDocs site locally."""
    try:
        print("Starting MkDocs development server...")
        print("Open http://127.0.0.1:8000 in your browser")
        subprocess.run([sys.executable, "-m", "mkdocs", "serve"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Server failed: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    main()