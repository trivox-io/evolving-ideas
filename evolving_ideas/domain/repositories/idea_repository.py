"""
evolving_ideas.domain.repositories.idea_repository
"""

from pathlib import Path
import os
from typing import List, Optional
import uuid
from datetime import datetime
import yaml

from evolving_ideas.domain.models.idea import IdeaVersion, QAPair, IdeaMetadata, Tree, NodeData
from evolving_ideas.domain.services.idea_tree import IdeaTree


class IdeaRepository:
    """
    Repository for managing ideas and their versions.
    This class provides methods to add, load, and list ideas stored in a directory.
    """
    
    def __init__(self, store_path: Path):
        """
        :param store_path: The path where ideas will be stored.
        :type store_path: Path
        """
        self.store_path = store_path
        os.makedirs(self.store_path, exist_ok=True)

    def add(self, role: str, task: str, qna: List[QAPair], summary: str, author: Optional[str], method: Optional[str], method_metadata: Optional[dict]) -> IdeaTree:
        """
        Adds a new idea to the repository.
        
        :param role: The role of the author (e.g., "developer", "designer").
        :type role: str
        
        :param task: The task or idea description.
        :type task: str
        
        :param qna: A list of question and answer pairs related to the idea.
        :type qna: List[QAPair]
        
        :param summary: A summary of the idea.
        :type summary: str
        
        :param author: The author of the idea (default is "santiago").
        :type author: str
        
        :return: An IdeaTree object representing the newly created idea.
        :rtype: IdeaTree
        """
        idea_id = f"idea_{str(uuid.uuid4())[:8]}"
        idea_dir = self.store_path / idea_id
        os.makedirs(idea_dir, exist_ok=True)

        now = datetime.now().isoformat()
        root_version = IdeaVersion(
            id=idea_id,
            version=1,
            title=task[:50],
            status="raw",
            created_at=now,
            author=author,
            parent_id=None,
            description=task,
            context={"role": role, "task": task, "notes": ""},
            qna=qna,
            attachments=[],
            tags=[],
            summary=summary,
            method=method,
            method_metadata=method_metadata or {},
        )
        root_version.to_file(idea_dir / "v1.yaml")
        
        metadata = IdeaMetadata(
            id=idea_id,
            title=root_version.title,
            created_by=author or "santiago",
            created_at=now,
            tree=Tree(
                root=1,
                current=1,
                children={"1": []}
            ),
            node_data={"1": NodeData(created_at=now, note=task, tags=[])}
        )

        (idea_dir / "metadata.yaml").write_text(yaml.safe_dump(metadata.to_dict(), sort_keys=False))
        return IdeaTree(idea_dir)

    def load(self, idea_id: str) -> IdeaTree:
        """
        Loads an idea from the repository by its ID.
        
        :param idea_id: The unique identifier of the idea to load.
        :type idea_id: str
        
        :return: An IdeaTree object representing the loaded idea.
        :rtype: IdeaTree
        
        :raises FileNotFoundError: If the idea with the given ID does not exist.
        """
        idea_dir = self.store_path / idea_id
        if not idea_dir.exists():
            raise FileNotFoundError(f"Idea {idea_id} does not exist.")
        return IdeaTree(idea_dir)

    def list(self) -> List[str]:
        """
        Lists all ideas stored in the repository.
        
        :return: A list of idea names (directories) in the store path.
        :rtype: List[str]
        """
        return [p.name for p in self.store_path.iterdir() if p.is_dir()]
