"""
evolving_ideas.strategies.six_hats
"""

from .base import MethodStrategy
from evolving_ideas.strategies.registry import Registry


class SixHatsMethod(MethodStrategy):
    """
    Strategy based on Edward de Bono's Six Thinking Hats.
    """

    HATS = {
        "White": "Focus on facts and data.",
        "Red": "Express feelings and intuitions.",
        "Black": "Identify risks, problems, and caution.",
        "Yellow": "Highlight benefits and value.",
        "Green": "Think creatively and explore alternatives.",
        "Blue": "Summarize, organize, and plan next steps."
    }

    def run(self, role: str, task: str, context: str) -> dict:
        qna = []
        for hat, description in self.HATS.items():
            self.logger.system(f"Thinking with the {hat} Hat: {description}")
            prompt = self.builder.build("six_hats_step", {
                "role": role,
                "task": task,
                "context": context,
                "hat": hat,
                "description": description
            })
            question = self.llm_responder.ask(prompt, context).strip()
            self.logger.assistant(question)

            answer = input("> ").strip()
            if answer:
                qna.append({"question": question, "answer": answer})
                self.logger.user(f"Answer: {answer}")

        self.logger.system("Summarizing Six Hats insights...")
        summary_prompt = self.builder.build("summarize_answers", {"qna": qna})
        summary = self.llm_responder.ask(summary_prompt, context)

        return {
            "qna": qna,
            "summary": summary,
            "method": "six_hats",
            "method_metadata": {"hats": list(self.HATS.keys())}
        }


Registry.register("six_hats", SixHatsMethod)
