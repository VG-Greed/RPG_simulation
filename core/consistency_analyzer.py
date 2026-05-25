from core.world_context import WorldContext
from core.json_parser import safe_json_loads

from llm.base_llm_client import BaseLLMClient

from agents.prompts.consistency_prompt import (
    CONSISTENCY_PROMPT
)


class ConsistencyAnalyzer:

    def __init__(
        self,
        llm_client: BaseLLMClient
    ):

        self.llm_client = llm_client

    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:

        language = context.user_requirements.get(
            "output_language",
            "russian"
        )

        prompt = CONSISTENCY_PROMPT.format(
            language=language,

            base_lore=context.base_lore_text,

            history=context.history_text,

            geography=context.geography_text,

            politics=context.politics_text,

            cultures=context.cultures_text
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You are an expert narrative "
                "consistency analyst for "
                "fantasy worldbuilding."
            ),

            model="gpt-4.1-mini",

            temperature=0,

            max_tokens=1500
        )

        parsed = safe_json_loads(
            response
        )

        context.consistency_report = parsed

        context.consistency_issues = parsed.get(
            "issues",
            []
        )

        print(
            "[ConsistencyAnalyzer] Completed"
        )

        return context