"""
evolving_ideas.cli
"""

import sys
import argparse
import os
from dotenv import load_dotenv

from evolving_ideas.app import EvolvingIdeaApp


load_dotenv()
VERSION = os.getenv("VERSION", "0.1.0")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BANNER = r"""
   _____            _              _____ _     _             
  | ____|_ ____   _(_) ___ ___    | ____| |__ (_)_ __   __ _ 
  |  _| | '__\ \ / / |/ __/ _ \   |  _| | '_ \| | '_ \ / _` |
  | |___| |   \ V /| | (_|  __/   | |___| | | | | | | | (_| |
  |_____|_|    \_/ |_|\___\___|   |_____|_| |_|_|_| |_|\__, |
                                                       |___/ 
      A CLI to capture, evolve, and expand your ideas.
"""


def main():
    """
    Main entry point for the Evolving Ideas CLI.
    """
    print(BANNER)
    print(f"Version: {VERSION}")
    parser = argparse.ArgumentParser(
        description="Evolving Ideas CLI - Capture and evolve your thoughts into structured systems."
    )
    parser.add_argument("-v", "--version", action="version", version=f"Evolving Ideas CLI v{VERSION}")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Add command
    subparsers.add_parser("add", help="Start a new idea from scratch")

    # Improve command
    improve_parser = subparsers.add_parser("improve", help="Improve a previously captured idea")
    improve_parser.add_argument("id", help="ID of the idea to improve")
    
    # evolve command
    evolve_parser = subparsers.add_parser("evolve", help="Evolve an idea into a more structured system")
    evolve_parser.add_argument("id", help="ID of the idea to evolve")

    # Parse args
    args = parser.parse_args()

    
    app = EvolvingIdeaApp()

    # Dispatch commands
    if args.command == "add":
        app.add()
    elif args.command == "improve":
        print("🚧 The 'improve' command is coming soon. Stay tuned!")
        sys.exit(0)
    elif args.command == "evolve":
        print("🚧 The 'evolve' command is coming soon. Stay tuned!")
        sys.exit(0)
