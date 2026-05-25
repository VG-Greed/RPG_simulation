from agents.base_agent import BaseAgent

from core.world_context import WorldContext

from llm.base_llm_client import BaseLLMClient

from agents.prompts.history_prompt import (
    HISTORY_PROMPT
)


class HistoryAgent(BaseAgent):

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

        prompt = HISTORY_PROMPT.format(
            language=language,

            base_lore=context.base_lore_text
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You are an expert fantasy "
                "historian and worldbuilding writer."
            ),

            model="gpt-4.1-mini",

            temperature=0.8,

            max_tokens=3000
        )

        context.history_text = response

        context.history_data = {
            "generated": True,

            "event_count": 5
        }

        print(
            "[HistoryAgent] Completed"
        )

        return context