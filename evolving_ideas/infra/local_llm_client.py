"""
evolving_ideas.infra.local_llm
"""

from typing import Optional

from transformers import pipeline

from evolving_ideas.infra.llm_interface import LLMInterface


class LocalLLM(LLMInterface):
    """
    A simple local LLM interface using Hugging Face Transformers.
    This is a naive implementation and can be improved with better prompt formatting.
    """

    def __init__(self, model_name: Optional[str] = "tiiuae/falcon-rw-1b"):
        """
        :param model_name: The name of the local model to use.
        :type model_name: str
        """

        self.generator = pipeline("text-generation", model=model_name)

    def ask(self, prompt: str, context: str) -> str:
        full_prompt = f"{context}\n\n{prompt}"
        result = self.generator(full_prompt, max_new_tokens=256, do_sample=True)[0][
            "generated_text"
        ]
        return str(result).strip()

    def chat(self, chatlog: list[dict]) -> str:
        # naive implementation, you can improve prompt formatting later
        conversation = "\n".join([f"{m['role']}: {m['content']}" for m in chatlog])
        return self.ask(conversation, context="You are a helpful assistant.")
