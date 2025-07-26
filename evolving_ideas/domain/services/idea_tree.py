"""
evolving_ideas.domain.services.ide_tree.py
"""

from pathlib import Path
import yaml

from evolving_ideas.domain.models.idea import IdeaVersion


class IdeaTree:
    """
    Represents a tree structure for an idea, including its versions and metadata.
    This class provides methods to manage the idea's versions and metadata.
    """

    def __init__(self, idea_dir: Path):
        """
        :param idea_dir: The directory where the idea and its versions are stored.
        :type idea_dir: Path
        """
        self.idea_dir = idea_dir
        self.meta_path = idea_dir / "metadata.yaml"
        self.metadata = yaml.safe_load(self.meta_path.read_text())
        self.versions = self._load_versions()

    def _load_versions(self) -> dict:
        """
        Loads all versions of the idea from the directory.
        
        :return: A dictionary mapping version numbers to IdeaVersion objects.
        :rtype: dict
        """
        return {
            int(f.stem[1:]): IdeaVersion.from_file(f)
            for f in self.idea_dir.glob("v*.yaml")
        }

    def add_version(self, version: IdeaVersion):
        """
        Adds a new version to the idea tree.
        
        :param version: The IdeaVersion object to add.
        :type version: IdeaVersion
        """
        version_file = self.idea_dir / f"v{version.version}.yaml"
        version.to_file(version_file)
        self.metadata["tree"]["children"].setdefault(str(version.parent_id), []).append(version.version)
        self.metadata["tree"]["current"] = version.version
        self.meta_path.write_text(yaml.safe_dump(self.metadata, sort_keys=False))

    def show_tree(self):
        """
        Displays the idea tree structure in a human-readable format.
        This method prints the idea's metadata and its version tree.
        """
        def walk(node, prefix=""):
            children = self.metadata["tree"]["children"].get(str(node), [])
            for child in children:
                print(f"{prefix}└── v{child}")
                walk(child, prefix + "    ")
        root = self.metadata["tree"]["root"]
        print(f"idea_{self.metadata['id']} (title: {self.metadata['title']})")
        print(f"└── v{root}")
        walk(root, prefix="    ")

    def add_new_version(self, new_version: IdeaVersion):
        """
        Adds a new version to the idea tree, ensuring it does not conflict with existing versions.
        
        :param new_version: The IdeaVersion object to add.
        :type new_version: IdeaVersion
        
        :raises ValueError: If the version already exists in the tree.
        """
        if new_version.version in self.versions:
            raise ValueError(f"Version {new_version.version} already exists")

        # Save the new version YAML
        version_file = self.idea_dir / f"v{new_version.version}.yaml"
        new_version.to_file(version_file)

        # Update metadata tree structure:
        parent = str(new_version.parent_id) if new_version.parent_id else str(self.metadata["tree"]["current"])
        if parent not in self.metadata["tree"]["children"]:
            self.metadata["tree"]["children"][parent] = []
        self.metadata["tree"]["children"][parent].append(new_version.version)

        self.metadata["tree"]["current"] = new_version.version
        self.versions[new_version.version] = new_version
        self.meta_path.write_text(yaml.safe_dump(self.metadata, sort_keys=False))
