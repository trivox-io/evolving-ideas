"""
evolving_ideas.prompts.builder
"""

import logging
from typing import Optional

from .template_store import PromptTemplateStore

logger = logging.getLogger(__name__)


class PromptBuilder:
    """
    Builds prompts by formatting a named template with dynamic context.
    """

    def __init__(self, store: Optional["PromptTemplateStore"] = None):
        """
        :param store: The store instance
        :type store: Optional[PromptTemplateStore]
        """
        logger.debug("Initializing PromptBuilder")
        self.store = store or PromptTemplateStore()

    def build(self, name: str, context: dict) -> str:
        """
        Build a prompt by formatting a template with the given context.

        :param name: The name of the template
        :type name: str

        :param context: The context to format the template with
        :type context: dict

        :return: Formatted context
        :rtype: str
        """
        template = self.store.get(name)
        if not template:
            raise ValueError(f"Prompt template '{name}' not found.")
        return template.format(**context)
