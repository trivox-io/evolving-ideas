"""
evolving_ideas.settings
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional

import yaml
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    Singleton for application settings.
    Supports .env and (future) YAML-based config.
    """
    _instance = None
    _data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._load()
        return cls._instance

    @classmethod
    def _load(cls):
        """
        Load settings from .env and YAML file.
        """
        cls._data = {
            "storage_path": ".storage/ideas",
            "cached_path": ".storage/cached.yml",
            "openai": {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "model": os.getenv("OPENAI_MODEL", "gpt-4")
            }
        }

        yaml_path = Path("config.yml")
        if yaml_path.exists():
            with yaml_path.open("r") as f:
                yaml_data = yaml.safe_load(f)
                cls._deep_merge(cls._data, yaml_data)

    @classmethod
    def _deep_merge(cls, base: Dict[str, Any], updates: Dict[str, Any]):
        """
        Recursively merge updates into base dictionary.
        """
        for k, v in updates.items():
            if isinstance(v, dict) and k in base:
                cls._deep_merge(base[k], v)
            else:
                base[k] = v

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Get a setting value by dot notation key (e.g., "openai.api_key").
        
        :param key: Dot-separated key path.
        :type key: str
        
        :param default: Fallback if key is not found.
        :type default: Optional[Any]
        
        :return: Value or default.
        :rtype: Any
        """
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def all(self) -> Dict[str, Any]:
        """
        Get all settings as a dictionary.
        
        :return: All settings.
        :rtype: Dict[str, Any]
        """
        return self._data


settings = Settings()
