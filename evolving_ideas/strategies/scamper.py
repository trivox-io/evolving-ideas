"""
evolving_ideas.strategies.scamper
"""

from evolving_ideas.strategies.registry import Registry

from .base import MethodStrategy


class ScamperMethod(MethodStrategy):
    """
    A strategy for the SCAMPER brainstorming technique.
    """

    SCAMPER_STEPS = [
        "Substitute",
        "Combine",
        "Adapt",
        "Modify",
        "Put to another use",
        "Eliminate",
        "Reverse",
    ]

    def run(self, role: str, task: str, context: str) -> dict:
        qna = []

        for step in self.SCAMPER_STEPS:
            self.logger.system(f"Applying SCAMPER: {step}")
            prompt = self.builder.build(
                "scamper_step",
                {"role": role, "task": task, "context": context, "step": step},
            )
            question = self.llm_responder.ask(prompt, context).strip()
            self.logger.assistant(question)

            answer = input("> ").strip()
            if answer:
                qna.append({"question": question, "answer": answer})
                self.logger.user(f"Answer: {answer}")

        self.logger.system("Summarizing SCAMPER results...")
        summary_prompt = self.builder.build("summarize_answers", {"qna": qna})
        summary = self.llm_responder.ask(summary_prompt, context)

        return {
            "qna": qna,
            "summary": summary,
            "method": "scamper",
            "method_metadata": {"steps": self.SCAMPER_STEPS},
        }


Registry.register("scamper", ScamperMethod)
