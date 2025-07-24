"""
evolving_ideas.prompts.template_store
"""
from pathlib import Path
import yaml


class PromptTemplateStore:
    """
    Singleton to load and cache prompt templates from YAML.
    """
    _instance = None
    _templates = {}

    def __new__(cls, path: Path = Path("evolving_ideas/prompts/templates.yml")):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load(path)
        return cls._instance

    @classmethod
    def _load(cls, path: Path):
        """Load prompt templates from a YAML file."""
        if not path.exists():
            raise FileNotFoundError(f"Prompt template file not found: {path}")
        with open(path, "r") as f:
            cls._templates = yaml.safe_load(f)

    def get(self, name: str) -> str:
        """
        Get a prompt template by name.
        
        :param name: The name of the template
        :type name: str
        
        :return: The template string
        :rtype: str
        """
        return self._templates.get(name)

    def all(self) -> dict:
        """
        Get all prompt templates.
        
        :return: All templates
        :rtype: dict
        """
        return self._templates
