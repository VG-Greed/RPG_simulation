from agents.base_agent import BaseAgent

from core.world_context import WorldContext

from llm.base_llm_client import BaseLLMClient

from agents.prompts.politics_prompt import (
    POLITICS_PROMPT
)


class PoliticsAgent(BaseAgent):

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

        prompt = POLITICS_PROMPT.format(
            language=language,

            base_lore=context.base_lore_text,

            history=context.history_text,

            geography=context.geography_text
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You are an expert fantasy political "
                "worldbuilding writer."
            ),

            model="gpt-4.1-mini",

            temperature=0.8,

            max_tokens=2500
        )

        context.politics_text = response

        context.politics_data = {
            "generated": True
        }

        print(
            "[PoliticsAgent] Completed"
        )

        return context