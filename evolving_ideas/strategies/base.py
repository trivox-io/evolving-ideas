"""
evolving_ideas.strategies.base
"""

from abc import ABC, abstractmethod
from typing import Optional

from evolving_ideas.infra.responder import LLMResponder
from evolving_ideas.interface.presenters import ChatLogger
from evolving_ideas.prompts.builder import PromptBuilder


class MethodStrategy(ABC):
    """
    Abstract base class for strategy methods in the evolving ideas application.
    This class defines the interface for all strategy methods that can be implemented
    for generating and evolving ideas.
    """

    builder: PromptBuilder

    def __init__(
        self,
        llm_responder: LLMResponder,
        builder: Optional[PromptBuilder] = None,
        chat_logger: Optional[ChatLogger] = None,
    ):
        """
        :param llm_responder: The LLM responder to use for generating responses.
        :type llm_responder: Optional[LLMResponder]

        :param builder: The prompt builder to use for generating prompts.
        :type builder: Optional[PromptBuilder]
        """
        self.llm_responder = llm_responder
        self.builder = builder or PromptBuilder()
        self.logger = chat_logger or ChatLogger()

    @abstractmethod
    def run(self, role: str, task: str, context: str) -> dict:
        """
        Abstract method to run the strategy with the given parameters.

        :param role: The role of the AI.
        :type role: str
        :param task: The task to be performed.
        :type task: str
        :param context: Context for the idea.
        :type context: str

        :return: A dictionary containing the results of the strategy.
        :rtype: dict
        """
