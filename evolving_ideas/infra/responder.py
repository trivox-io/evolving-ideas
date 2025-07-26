"""
evolving_ideas.infra.responder
"""

import logging

from evolving_ideas.infra.open_ai_client import OpenAILLM
from evolving_ideas.settings import settings

logger = logging.getLogger(__name__)


class LLMResponder:
    """
    Wraps the underlying LLM for easier substitution/testing.
    """

    def __init__(self):
        logger.debug("Initializing LLM Responder")
        config: dict = settings.get("openai")
        self.llm = OpenAILLM(model=config.get("model"), api_key=config.get("api_key"))

    def ask(self, prompt: str, context="You are a helpful assistant.") -> str:
        """
        Ask the LLM a question with a given prompt and context.

        :param prompt: The prompt to send to the LLM.
        :type prompt: str

        :param context: Additional context for the LLM (default is "You are a helpful assistant.").
        :type context: str

        :return: The LLM's response.
        :rtype: str
        """
        return self.llm.ask(prompt, context)

    def chat(self, chatlog: list) -> str:
        """
        Start a chat session with the LLM.

        :param chatlog: A list of messages to include in the chat context.
        :type chatlog: list

        :return: The LLM's response.
        :rtype: str
        """
        return self.llm.chat(chatlog)
