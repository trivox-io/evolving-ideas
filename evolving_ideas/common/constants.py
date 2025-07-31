"""
evolving_ideas.common.constants
"""

import os

from dotenv import load_dotenv

load_dotenv()
VERSION = os.getenv("VERSION", "0.2.0")
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
