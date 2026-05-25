from agents.base_agent import BaseAgent

from core.world_context import WorldContext

from llm.base_llm_client import BaseLLMClient

from prompts.cultures_prompt import (
    CULTURES_PROMPT
)


class CulturesAgent(BaseAgent):

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

        prompt = CULTURES_PROMPT.format(
            language=language,

            base_lore=context.base_lore_text,

            history=context.history_text,

            geography=context.geography_text,

            politics=context.politics_text
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You are an expert fantasy "
                "culture and religion designer."
            ),

            model="gpt-4.1-mini",

            temperature=0.9,

            max_tokens=2500
        )

        context.cultures_text = response

        context.cultures_data = {
            "generated": True
        }

        print(
            "[CulturesAgent] Completed"
        )

        return context