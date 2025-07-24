"""
evolving_ideas.strategies.classic
"""

from .base import MethodStrategy
from evolving_ideas.strategies.registry import Registry


class ClassicMethod(MethodStrategy):
    """
    A strategy for classic brainstorming techniques.
    """

    def run(self, role: str, task: str, context: str) -> dict:
        self.logger.system("Running classic brainstorming method...")
        prompt = self.builder.build("ask_questions", {"role": role, "task": task, "context": context})
        questions_text = self.llm_responder.ask(prompt, context)
        questions = [q.strip("- ").strip() for q in questions_text.split("\n") if q.strip()]

        qna = []
        for q in questions:
            self.logger.assistant(q)
            answer = input("> ").strip()
            if answer:
                qna.append({"question": q, "answer": answer})
                self.logger.user(f"Answer: {answer}")

        self.logger.system("Summarizing idea...")
        summary_prompt = self.builder.build("summarize_answers", {"qna": qna})
        summary = self.llm_responder.ask(summary_prompt, context)

        return {
            "qna": qna,
            "summary": summary,
            "method": "classic",
            "method_metadata": {"raw_prompt": prompt, "raw_response": questions_text}
        }


Registry.register("classic", ClassicMethod)
