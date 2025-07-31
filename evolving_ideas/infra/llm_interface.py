"""
evolving_ideas.infra.llm_interface
"""

from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """
    Abstract base class for LLM interfaces.
    """

    @abstractmethod
    def ask(self, prompt: str, context: str = "You are a helpful assistant.") -> str:
        """
        Ask the LLM a question with a given prompt and context.

        :param prompt: The prompt to send to the LLM.
        :type prompt: str

        :param context: Additional context for the LLM (default is "You are a helpful assistant.").
        :type context: str

        :return: The LLM's response.
        :rtype: str
        """

    @abstractmethod
    def chat(self, chatlog: list) -> str:
        """
        Start a chat session with the LLM.

        :param chatlog: A list of messages to include in the chat context.
        :type chatlog: list

        :return: The LLM's response.
        :rtype: str
        """
