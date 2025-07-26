"""
evolving_ideas.strategies.router
"""

METHOD_KEYWORDS = {
    "scamper": ["refactor", "rethink", "transform", "improve", "modify", "adapt"],
    "lotus_blossom": ["expand", "breakdown", "areas", "categories", "dimensions"],
    "six_hats": ["perspective", "alternatives", "risk", "judgment", "feelings"],
    "classic": [],
}


def select_method(task: str) -> str:
    """
    Selects a brainstorming method based on keywords in the task description.

    :param task: The task description to analyze.
    :type task: str

    :return: The name of the selected method.
    :rtype: str
    """
    task_lower = task.lower()

    for method, keywords in METHOD_KEYWORDS.items():
        if any(word in task_lower for word in keywords):
            return method

    return "classic"
