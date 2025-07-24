"""
evolving_ideas.app
"""

import os
import logging
from pathlib import Path
from typing import Optional

from evolving_ideas.common.logger import setup_logging
from evolving_ideas.settings import settings
from evolving_ideas.interface.presenters import chat_logger
from evolving_ideas.domain.repositories.idea_repository import IdeaRepository
from evolving_ideas.domain.models.idea import QAPair
from evolving_ideas.domain.services.ide_tree import IdeaTree
from evolving_ideas.infra.responder import LLMResponder
from evolving_ideas.sessions.chat import ChatSession

from evolving_ideas.common.cache_store import CacheStore


setup_logging(logging.DEBUG)
logger = logging.getLogger(__name__)


class InputCollector:
    """
    Collects user inputs for the idea creation process.
    """
    
    def __init__(self):
        self.cache = CacheStore()

    def collect(self) -> dict:
        """
        Collects user inputs for the idea.
        
        :return: A dictionary containing the user inputs.
        :rtype: dict
        """
        inputs = {
            "author": self._get_author(),
            "role": self._prompt("Who should the AI act like?", default="Assistant"),
            "task": self._prompt("What are you working on?", required=True),
        }

        context = self._prompt("What context should the AI have?")
        if not context:
            context = f"You are a helpful assistant acting as a {inputs['role']}."
        elif inputs["role"] not in context:
            context += f" You are acting as a {inputs['role']}."
        inputs["context"] = context

        return inputs

    def _get_author(self) -> str:
        cached_name = self.cache.get("author")
        if cached_name:
            return cached_name
        chat_logger.system("What's your name?")
        name = input("> ").strip().lower() or os.getlogin().lower()
        self.cache.set("author", name)
        return name

    def _prompt(self, message: str, default: str = "", required: bool = False) -> str:
        chat_logger.system(message)
        while True:
            response = input("> ").strip()
            if response:
                return response
            if default:
                return default
            if not required:
                return ""
            logger.warning("This field is required.")


class EvolvingIdeaApp:
    """
    Main application class for the Ideas app.
    """
    
    def __init__(self, llm_responder: Optional[LLMResponder] = None):
        """
        Initializes the EvolvingIdeaApp with an optional LLM Responder.
        
        :param llm_responder: The LLM responder to use for generating responses.
        :type llm_responder: LLMResponder
        """
        if not llm_responder:
            llm_responder = LLMResponder()
        self.session = ChatSession(llm_responder=llm_responder)
        self.input_collector = InputCollector()
        logger.debug("EvolvingIdeaApp initialized with LLM Responder")

    def add(self) -> dict:
        """
        Start the Ideas app.
        
        :return: A dictionary containing the role, task, Q&A pairs, and summary of the idea.
        :rtype: dict
        """
        logger.debug("Welcome to the Ideas App! Let's brainstorm your ideas.")

        inputs = self.input_collector.collect()
        author = inputs["author"]
        
        logger.debug(f"Collected inputs: {inputs}")

        idea_data = self.session.run(role=inputs.get("role"), task=inputs.get("task"), context=inputs.get("context"))

        repo = IdeaRepository(Path(settings.get("storage_path")))
        idea_tree = repo.add(
            role=idea_data["role"],
            task=idea_data["task"],
            qna=[QAPair(**qa) for qa in idea_data["qna"]],
            summary=idea_data["summary"],
            author=author,
            method=idea_data["method"],
            method_metadata=idea_data["method_metadata"]
        )
        chat_logger.system(f"New idea created with ID: {idea_tree.metadata['id']}")
        
        return idea_data

    def load(self, idea_id: str) -> IdeaTree:
        """
        Loads an idea by its ID from the repository.
        
        :param idea_id: The unique identifier of the idea to load.
        :type idea_id: str
        
        :return: An IdeaTree object representing the loaded idea.
        :rtype: IdeaTree
        """
        repo = IdeaRepository(Path(".storage/applications/ideas"))
        return repo.load(idea_id)

    def improve(self, idea_id: str):
        """
        Improves an existing idea version by running a chat session to gather input.
        
        :param idea_id: The unique identifier of the idea to improve.
        :type idea_id: str
        """
        # idea_tree = self.load(idea_id)
        # parent_version_obj = idea_tree.versions.get(parent_version)
        # if not parent_version_obj:
        #     logging.error(f"Parent version {parent_version} not found.")
        #     return

        # # Run chat session or gather input for improved idea version
        # idea_data = self.run_chat_session()

        # new_version_num = max(idea_tree.versions.keys()) + 1
        # new_version = IdeaVersion(
        #     id=idea_id,
        #     version=new_version_num,
        #     title=idea_data["task"][:50],
        #     status="raw",
        #     created_at=datetime.now().isoformat(),
        #     author=parent_version_obj.author,
        #     parent_id=parent_version,
        #     description=idea_data["task"],
        #     context={"role": idea_data["role"], "task": idea_data["task"], "notes": ""},
        #     qna=[QAPair(**qa) for qa in idea_data["qna"]],
        #     attachments=[],
        #     tags=[],
        #     linked_projects=[],
        #     related_ideas=[]
        # )
        # idea_tree.add_new_version(new_version)
        # logging.info(f"Added new version v{new_version_num} to idea {idea_id}")
