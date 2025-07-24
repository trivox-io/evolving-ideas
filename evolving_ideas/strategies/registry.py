"""
evolving_ideas.strategies.registry
"""

from typing import Type, Optional


class Registry:
    """
    A registry for storing and managing strategies.
    """
    
    strategies = {}

    @classmethod
    def register(cls, name: str, strategy: Type):
        """
        Register a new strategy.

        :param name: The name of the strategy.
        :param strategy: The strategy class.
        """
        cls.strategies[name] = strategy

    @classmethod
    def get(cls, name: str, *args, **kwargs) -> Optional[Type]:
        """
        Get a registered strategy by name.

        :param name: The name of the strategy.
        :return: The strategy class or None if not found.
        """
        return cls.strategies.get(name)(*args, **kwargs)
