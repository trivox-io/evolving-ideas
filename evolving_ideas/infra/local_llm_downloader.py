"""
evolving_ideas.infra.local_llm_downloader
"""

import logging
from typing import Optional

from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


# TODO: This should come from settings or be configurable
MODEL_NAME = "sshleifer/tiny-gpt2"
SAVE_DIRECTORY = "./.models/tiny-gpt2"


class LocalLLMDownloader:
    """
    Downloads and saves the local LLM model and tokenizer.
    """

    def __init__(
        self,
        model_name: Optional[str] = MODEL_NAME,
        save_directory: str = SAVE_DIRECTORY,
    ):
        self.model_name = model_name
        self.save_directory = save_directory

    def download(self):
        """
        Downloads the model and tokenizer, saving them to the specified directory.
        """
        logger.info(f"Downloading model {self.model_name} to {self.save_directory}")
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = AutoModelForCausalLM.from_pretrained(self.model_name)

            tokenizer.save_pretrained(self.save_directory)
            model.save_pretrained(self.save_directory)

            logger.info(f"Model and tokenizer saved to {self.save_directory}")
        except Exception as e:
            logger.error("❌ Failed to download model.")
            logger.exception(e)
            # Suggest cleanup step
            logger.info(
                "You may need to delete .cache/huggingface/hub/.locks and retry."
            )
