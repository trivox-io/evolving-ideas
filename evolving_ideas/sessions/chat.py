"""
evolving_ideas.sessions.chat
"""

import logging
from typing import Optional
from evolving_ideas.infra.responder import LLMResponder
from evolving_ideas.prompts.builder import PromptBuilder
from evolving_ideas.interface.presenters import ChatLogger

from evolving_ideas.strategies.router import select_method
from evolving_ideas.strategies.base import MethodStrategy
from evolving_ideas.strategies.registry import Registry

logger = logging.getLogger(__name__)


class ChatSession:
    """
    Runs a single chat session for creating or improving ideas.
    """

    def __init__(self, llm_responder: LLMResponder, builder: Optional[PromptBuilder] = None, chat_logger: Optional[ChatLogger] = None):
        """
        :param llm_responder: The LLM responder to use for generating responses.
        :type llm_responder: Optional[LLMResponder]
        
        :param builder: The prompt builder to use for generating prompts.
        :type builder: Optional[PromptBuilder]
        """
        self.llm_responder = llm_responder
        self.builder = builder or PromptBuilder()
        self.logger = chat_logger or ChatLogger()
        logger.debug("Initialized ChatSession with LLM Responder and Prompt Builder")

    def run(self, role: str, task: str, context: Optional[str] = None) -> dict:
        """
        Runs the chat session to create or improve an idea.
        
        :param role: The role the AI should assume (e.g., "assistant", "expert").
        :type role: str
        
        :param task: The task or idea the user is working on.
        :type task: str
        
        :return: A dictionary containing the role, task, Q&A pairs, and summary of the idea.
        :rtype: dict
        """
        if not context:
            context = "You are a helpful assistant."
        self.logger.system("Generating follow-up questions...")
        method = select_method(task)
        strategy: MethodStrategy = Registry.get(method, self.llm_responder, self.builder, self.logger)
        result = strategy.run(role, task, context)

        return {
            "role": role,
            "task": task,
            "context": context,
            "qna": result["qna"],
            "summary": result["summary"],
            "method": method,
            "method_metadata": result.get("method_metadata", {})
        }
