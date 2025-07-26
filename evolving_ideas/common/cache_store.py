"""
evolving_ideas.common.cache_store
"""

import logging
from pathlib import Path
from typing import Any, Optional

import yaml

from evolving_ideas.settings import settings

logger = logging.getLogger(__name__)


class CacheStore:
    """
    A lightweight key-value cache backed by a YAML file.
    Used for caching settings like valid API key or username.
    """

    def __init__(self, path: Optional[str] = None):
        self.cache_path = Path(path or settings.get("cached_path"))
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self._data = self._load()

    def _load(self) -> dict:
        if self.cache_path.exists():
            try:
                with self.cache_path.open("r") as f:
                    return yaml.safe_load(f) or {}
            except Exception as e:
                logger.warning(f"Could not read cache file: {e}")
        return {}

    def _save(self):
        try:
            with self.cache_path.open("w") as f:
                yaml.safe_dump(self._data, f, sort_keys=False)
        except Exception as e:
            logger.warning(f"Could not write cache file: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any):
        self._data[key] = value
        self._save()
        logger.debug(f"Cached [{key}] = {value} to {self.cache_path}")

    def delete(self, key: str):
        if key in self._data:
            del self._data[key]
            self._save()

    def all(self) -> dict:
        return self._data

    def clear(self):
        self._data = {}
        self._save()
        logger.info(f"Cache cleared at {self.cache_path}")
