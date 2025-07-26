"""
evolving_ideas.strategies.lotus_blossom
"""

from evolving_ideas.strategies.registry import Registry

from .base import MethodStrategy


class LotusBlossomMethod(MethodStrategy):
    """
    A strategy for the Lotus Blossom brainstorming technique.
    """

    def run(self, role: str, task: str, context: str) -> dict:
        self.logger.system("Starting Lotus Blossom technique...")

        # Step 1: Get 8 core related ideas
        core_prompt = self.builder.build(
            "lotus_core_ideas", {"role": role, "task": task, "context": context}
        )
        core_response = self.llm_responder.ask(core_prompt, context)
        core_ideas = [
            line.strip("-• ").strip()
            for line in core_response.split("\n")
            if line.strip()
        ]
        self.logger.system("Core branches:")
        for idea in core_ideas:
            self.logger.assistant(f"- {idea}")

        qna = [
            {"question": "What are 8 related ideas?", "answer": core_response.strip()}
        ]

        # Step 2: Expand each core idea
        expansion_map = {}
        for idea in core_ideas:
            self.logger.system(f"Expanding idea: {idea}")
            sub_prompt = self.builder.build(
                "lotus_sub_ideas",
                {"role": role, "task": task, "context": context, "idea": idea},
            )
            sub_response = self.llm_responder.ask(sub_prompt, context)
            sub_ideas = [
                line.strip("-• ").strip()
                for line in sub_response.split("\n")
                if line.strip()
            ]
            expansion_map[idea] = sub_ideas
            qna.append(
                {
                    "question": f"What are 8 sub-ideas for '{idea}'?",
                    "answer": sub_response.strip(),
                }
            )

        self.logger.system("Summarizing Lotus Blossom output...")
        summary_prompt = self.builder.build("summarize_answers", {"qna": qna})
        summary = self.llm_responder.ask(summary_prompt, context)

        return {
            "qna": qna,
            "summary": summary,
            "method": "lotus_blossom",
            "method_metadata": {
                "core_ideas": core_ideas,
                "expansion_map": expansion_map,
            },
        }


Registry.register("lotus_blossom", LotusBlossomMethod)
