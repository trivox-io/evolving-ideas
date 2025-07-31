"""
evolving_ideas.infra.responder
"""

import logging

from evolving_ideas.infra.llm_interface import LLMInterface
from evolving_ideas.infra.local_llm_client import LocalLLM
from evolving_ideas.infra.open_ai_client import OpenAILLM
from evolving_ideas.settings import settings

logger = logging.getLogger(__name__)

LLM_BACKENDS = {"openai": OpenAILLM, "local": LocalLLM}


def get_llm_backend(name: str) -> LLMInterface:
    try:
        return LLM_BACKENDS[name]
    except KeyError as e:
        raise ValueError(f"Unsupported LLM backend: {name}") from e


class LLMResponder:
    """
    Wraps the underlying LLM for easier substitution/testing.
    """

    llm: LLMInterface

    def __init__(self):
        logger.debug("Initializing LLM Responder")

        backend = settings.get("llm.backend", "local")
        model = settings.get("llm.model", "tiiuae/falcon-rw-1b")

        llm_class = get_llm_backend(backend)
        self.llm = llm_class(model_name=model)

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
