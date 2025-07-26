"""
evolving_ideas.domain.models.idea
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import yaml


@dataclass
class Attachment:
    """
    Represents an attachment for an idea version.

    :cvar path: str: The file path of the attachment.
    :cvar description: str: A brief description of the attachment.
    """

    path: str
    description: str


@dataclass
class QAPair:
    """
    Represents a question and answer pair for an idea version.

    :cvar question: str: The question asked about the idea.
    :cvar answer: str: The answer provided for the question.
    """

    question: str
    answer: str


@dataclass
class IdeaVersion:
    """
    Represents a version of an idea.

    :cvar id: str: Unique identifier for the idea.
    :cvar version: int: The version number of the idea.
    :cvar title: str: The title of the idea.
    :cvar status: str: The current status of the idea (e.g., "raw", "in progress", "completed").
    :cvar created_at: str: The timestamp when the idea version was created.
    :cvar author: str: The author of the idea version.
    :cvar parent_id: Optional[int]: The ID of the parent version, if applicable.
    :cvar description: str: A detailed description of the idea.
    :cvar context: dict: Additional context for the idea, such as role and task.
    :cvar qna: List[QAPair]: A list of question and answer pairs related to the idea.
    :cvar attachments: List[Attachment]: A list of attachments related to the idea.
    :cvar tags: List[str]: Tags associated with the idea for categorization.
    :cvar linked_projects: List[str]: Projects that this idea is linked to.
    :cvar related_ideas: List[str]: Other ideas that are related to this one.
    """

    id: str
    version: int
    title: str
    status: str
    created_at: str
    author: str
    parent_id: Optional[str]
    description: str
    context: dict
    qna: List[QAPair]
    attachments: List[Attachment]
    tags: List[str]
    summary: str = ""
    method: Optional[str] = None
    method_metadata: Optional[dict] = None

    # TODO - Add these fields in the future
    # linked_projects: List[str] = None
    # related_ideas: List[str] = None

    @classmethod
    def from_file(cls, path: Path) -> "IdeaVersion":
        """
        Load an IdeaVersion from a YAML file.

        :param path: The path to the YAML file.
        :type path: Path

        :return: An IdeaVersion object loaded from the file.
        :rtype: IdeaVersion
        """
        data = yaml.safe_load(path.read_text())
        return cls(**data)

    def to_file(self, path: Path):
        """
        Save the IdeaVersion to a YAML file.

        :param path: The path where the YAML file will be saved.
        :type path: Path
        """
        data = self.__dict__
        data["qna"] = [qa.__dict__ for qa in self.qna]
        data["attachments"] = [att.__dict__ for att in self.attachments]
        path.write_text(yaml.safe_dump(data, sort_keys=False))


@dataclass
class Tree:
    """
    Represents the version tree of an idea.

    :cvar root: int: The ID of the root version.
    :cvar current: int: The ID of the current version.
    :cvar children: dict: A dictionary mapping version IDs to their child versions.
    """

    root: int
    current: int
    children: dict[str, List[int]]


@dataclass
class NodeData:
    """
    Represents a node in the idea tree.

    :cvar created_at: str: The timestamp when the node was created.
    :cvar note: str: A note or description for the node.
    """

    created_at: str
    note: str
    tags: List[str]


@dataclass
class IdeaMetadata:
    """
    Represents metadata for an idea.

    :cvar id: str: Unique identifier for the idea.
    :cvar title: str: The title of the idea.
    :cvar created_by: str: The author of the idea.
    :cvar created_at: str: The timestamp when the idea was created.
    :cvar tree: dict: Metadata about the idea's version tree.
    """

    id: str
    title: str
    created_by: str
    created_at: str
    tree: Tree
    node_data: dict[str, NodeData]

    def to_dict(self) -> dict:
        """
        Convert the IdeaMetadata to a dictionary.

        :return: A dictionary representation of the IdeaMetadata.
        :rtype: dict
        """
        return {
            "id": self.id,
            "title": self.title,
            "created_by": self.created_by,
            "created_at": self.created_at,
            "tree": self.tree.__dict__,
            "node_data": {k: v.__dict__ for k, v in self.node_data.items()},
        }
