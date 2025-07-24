"""
Strategies for idea evolution.
"""

from evolving_ideas.strategies.base import MethodStrategy
from evolving_ideas.strategies.classic import ClassicMethod
from evolving_ideas.strategies.scamper import ScamperMethod
from evolving_ideas.strategies.router import select_method
from evolving_ideas.strategies.registry import Registry
