"""
evolving_ideas.interface.presenters
"""

from enum import Enum


class ChatPresenterRoles(Enum):
    """
    Enum-like class to define roles for chat messages.
    This class is used to categorize the roles of participants in a chat session.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class ChatPresenterRoleIcons(Enum):
    """
    Enum-like class to define icons for chat roles.
    This class is used to represent different roles in a chat session with icons.
    """

    SYSTEM = "🧠"
    USER = "👤"
    ASSISTANT = "🤖"


class ChatLogger:
    """
    A class to present chat messages in a structured format.
    This class is used to format and display chat messages in the application.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(ChatLogger, cls).__new__(cls)
        return cls.instance

    def log(self, message: str, role: ChatPresenterRoles = ChatPresenterRoles.USER):
        """
        Log a chat message with a specific role.

        :param message: The message to log.
        :type message: str

        :param role: The role of the sender (default is "user").
        :type role: str
        """
        print(
            f"{ChatPresenterRoleIcons[role.name].value} {role.value.capitalize()}: {message}"
        )

    def system(self, message: str):
        """
        Log a system message.

        :param message: The system message to log.
        :type message: str
        """
        self.log(message, role=ChatPresenterRoles.SYSTEM)

    def user(self, message: str):
        """
        Log a user message.

        :param message: The user message to log.
        :type message: str
        """
        self.log(message, role=ChatPresenterRoles.USER)

    def assistant(self, message: str):
        """
        Log an assistant message.

        :param message: The assistant message to log.
        :type message: str
        """
        self.log(message, role=ChatPresenterRoles.ASSISTANT)


chat_logger = ChatLogger()
