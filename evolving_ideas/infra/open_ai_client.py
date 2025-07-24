"""
evolving_ideas.infra.open_ai_client
"""

import logging
from typing import Optional
from functools import wraps

import openai

from evolving_ideas.common.cache_store import CacheStore
from evolving_ideas.interface.presenters import chat_logger


logger = logging.getLogger(__name__)
cache = CacheStore()


class OpenAIClientError(Exception):
    """
    Custom exception for OpenAI client errors.
    """


class OpenAITransport:
    """
    OpenAI client for interacting with the OpenAI API.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        :param api_key: The OpenAI API key.
        :type api_key: str
        
        :raises ValueError: If the API key is not provided.
        """
        logger.debug("Initializing OpenAITransport with API key.")
        self.client = openai.OpenAI(api_key=api_key)
        self.__check_key(api_key)

    def __check_key(self, api_key: str) -> bool:
        """
        Check if the provided API key is valid.
        
        :param api_key: The OpenAI API key.
        :type api_key: str

        :return: True if the API key is valid, False otherwise.
        :rtype: bool
        
        :raises ValueError: If the API key is invalid.
        """
        
        if api_key is None:
            raise ValueError("API key is required.")

        try:
            self.client.models.list()
        except openai.AuthenticationError as e:
            print(f"Authentication error: {e}")
            raise ValueError("Invalid API key provided.") from e

    def get_models(self) -> dict:
        """
        # Get the available models from OpenAI.

        :return: A dictionary categorizing available models.
        :rtype: dict
        """

        models = self.client.models.list()

        text_generation_models = []
        image_generation_models = []
        text_to_speech_models = []
        speech_recognition_models = []
        embedding_models = []

        for model in models:
            print(model, "\n")
            model_id = model.id
            # Check for text generation models
            if any(
                keyword in model_id
                for keyword in ["gpt", "chatgpt", "davinci", "babbage"]
            ):
                text_generation_models.append(model_id)
            # Check for image generation models
            elif "dall-e" in model_id:
                image_generation_models.append(model_id)
            # Check for text-to-speech models
            elif "tts" in model_id:
                text_to_speech_models.append(model_id)
            # Check for speech recognition models
            elif "whisper" in model_id:
                speech_recognition_models.append(model_id)
            # Check for embedding models
            elif "embedding" in model_id:
                embedding_models.append(model_id)

        return {
            "text_generation": text_generation_models,
            "image_generation": image_generation_models,
            "text_to_speech": text_to_speech_models,
            "speech_recognition": speech_recognition_models,
            "embedding": embedding_models,
        }

    def chat_completion(self, model: str, messages: list, temperature: float = 0.7) -> dict:
        """
        Chat completion using the OpenAI API.
        
        :param model: The model to use (e.g., "gpt-4").
        :type model: str
        
        :param messages: The messages to send to the model.
        :type messages: list
        
        :param temperature: The temperature for the model (default is 0.7).
        :type temperature: float
        
        :return: The response from the model.
        :rtype: dict
        """
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )

    def create_thread(self):
        """
        Create a new thread for the OpenAI API.
        """
        raise NotImplementedError("Thread creation is not implemented yet.")

    def run_thread(self, assistant_id: str, thread_id: str):
        """
        Run a thread for the OpenAI API.
        
        :param assistant_id: The ID of the assistant.
        :type assistant_id: str
        
        :param thread_id: The ID of the thread.
        :type thread_id: str
        """
        raise NotImplementedError("Thread running is not implemented yet.")

    def add_message(self, thread_id: str, role: str, content: str):
        """
        Add a message to a thread.
        
        :param thread_id: The ID of the thread.
        :type thread_id: str
        
        :param role: The role of the message sender (e.g., "user", "assistant").
        :type role: str
        
        :param content: The content of the message.
        :type content: str
        """
        raise NotImplementedError("Adding messages to a thread is not implemented yet.")

    def get_messages(self, thread_id: str):
        """
        Get messages from a thread.
        
        :param thread_id: The ID of the thread.
        :type thread_id: str
        """
        raise NotImplementedError("Getting messages from a thread is not implemented yet.")


def cached_validation_wrapper(key: str = "valid_api_key"):
    """
    Decorator to check for a cached validation flag before executing a function.

    :param key: Key in the cached file to verify.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache = CacheStore()
            cached = cache.get(key)

            if cached is None:
                try:
                    result = func(*args, **kwargs)
                    cache.set(key, True)
                    return result
                except Exception as e:
                    cache.set(key, False)
                    raise ValueError(f"Cached validation failed for key: {key}") from e

            if cached is False:
                raise ValueError(f"Cached validation failed for key: {key}")

            return True  # cached is True
        return wrapper
    return decorator


class OpenAICredentialValidator:
    """
    Validates OpenAI API credentials.
    """
    
    def __init__(self, client: openai.OpenAI):
        """
        :param client: The OpenAI client instance.
        :type client: openai.OpenAI
        """
        logger.debug("Initializing OpenAICredentialValidator.")
        self.client = client

    @cached_validation_wrapper("valid_api_key")
    def validate(self) -> bool:
        """
        Validate the OpenAI API key.
        
        :return: True if the API key is valid, False otherwise.
        :rtype: bool
        
        :raises OpenAIClientError: If the API key is invalid.
        """
        try:
            self.client.models.list()
            cache.set("valid_api_key", True)
            return True
        except openai.AuthenticationError as e:
            print(f"Authentication error: {e}")
            raise OpenAIClientError("Invalid API key.") from e


class OpenAILLM:
    """
    OpenAI Language Model Wrapper
    """
    
    name: str = "openai"
    
    def __init__(self, model="gpt-4.1", transport: Optional[OpenAITransport] = None, **kwargs):
        """
        :param model: The model to use (default is "gpt-4.1").
        :type model: str
        
        :param transport: The transport layer for API communication.
        :type transport: OpenAITransport
        """
        if transport is None:
            api_key = kwargs.get("api_key")
            transport = OpenAITransport(api_key)
        self.model = model
        self.transport = transport
        self._validator = OpenAICredentialValidator(self.transport.client)
        
        logger.debug(f"Initialized OpenAILLM with model: {self.model}")
        
        self.__validate()

    def __validate(self):
        """
        Validate the OpenAI API key.
        
        :raises ValueError: If the API key is invalid.
        """
        try:
            self._validator.validate()
            logger.debug("OpenAI API key is valid.")
        except OpenAIClientError as e:
            raise ValueError(f"Invalid API key: {e}") from e

    def ask(self, prompt: str, context: Optional[str] = "You are a helpful assistant.") -> str:
        """
        Ask the OpenAI model a question and return the answer.
        
        :param prompt: The question to ask.
        :type prompt: str
        
        :param role: The role of the user (e.g., "user", "assistant").
        :type role: str
        
        :param content: The content of the message.
        :type content: str
        
        :return: The answer from the model.
        :rtype: str
        """
        chat_logger.user(prompt)
        messages = [
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ]
        response = self.transport.chat_completion(model=self.model, messages=messages)
        return response.choices[0].message.content.strip()

    def chat(self, chatlog: list[dict]) -> str:
        """
        Chat with the OpenAI model using a chat log.
        
        :param chatlog: The chat log to send to the model.
        :type chatlog: list[dict]
        
        :return: The response from the model.
        :ytype: str
        """
        response = self.transport.chat_completion(model=self.model, messages=chatlog)
        return response.choices[0].message.content.strip()
