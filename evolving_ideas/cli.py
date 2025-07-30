"""
evolving_ideas.cli
"""

import argparse
import os
import sys

from dotenv import load_dotenv

from evolving_ideas.app import EvolvingIdeaApp, SettingsApp
from evolving_ideas.infra.local_llm_downloader import LocalLLMDownloader

load_dotenv()
VERSION = os.getenv("VERSION", "0.1.0")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BANNER = r"""
     _____           _       _               _____    _                 
    |  ___|         | |     (_)             |_   _|  | |                
    | |____   _____ | |_   ___ _ __   __ _    | |  __| | ___  __ _ ___  
    |  __\ \ / / _ \| \ \ / / | '_ \ / _` |   | | / _` |/ _ \/ _` / __| 
    | |___\ V / (_) | |\ V /| | | | | (_| |  _| || (_| |  __/ (_| \__ \ 
    \____/ \_/ \___/|_| \_/ |_|_| |_|\__, |  \___/\__,_|\___|\__,_|___/ 
                                      __/ |                             
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
    parser.add_argument(
        "-v", "--version", action="version", version=f"Evolving Ideas CLI v{VERSION}"
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # Add command
    subparsers.add_parser("add", help="Start a new idea from scratch")

    # Improve command
    improve_parser = subparsers.add_parser(
        "improve", help="Improve a previously captured idea"
    )
    improve_parser.add_argument("id", help="ID of the idea to improve")

    # evolve command
    evolve_parser = subparsers.add_parser(
        "evolve", help="Evolve an idea into a more structured system"
    )
    evolve_parser.add_argument("id", help="ID of the idea to evolve")

    settings_parser = subparsers.add_parser(
        "settings", help="View or modify application settings"
    )
    settings_parser.add_argument(
        "--view", action="store_true", help="View current settings"
    )

    subparsers.add_parser(
        "download-model", help="Download the local LLM model and tokenizer"
    )

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
    elif args.command == "settings":
        settings_app = SettingsApp()
        if args.view:
            settings_app.view()
    elif args.command == "download-model":
        downloader = LocalLLMDownloader()
        downloader.download()
