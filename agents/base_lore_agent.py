import json

from agents.base_agent import BaseAgent

from core.world_context import WorldContext

from llm.base_llm_client import BaseLLMClient

from prompts.base_lore_prompt import (
    BASE_LORE_PROMPT
)


class BaseLoreAgent(BaseAgent):

    def __init__(
        self,
        llm_client: BaseLLMClient
    ):

        self.llm_client = llm_client

    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:

        requirements_json = json.dumps(
            context.user_requirements,
            indent=2
        )

        language = context.user_requirements.get(
            "output_language",
            "russian"
        )

        prompt = BASE_LORE_PROMPT.format(
            requirements=requirements_json,
            language=language
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You are an expert fantasy "
                "worldbuilding writer "
                "specializing in tabletop RPGs."
            ),

            model="gpt-4.1-mini",

            temperature=0.9,

            max_tokens=3000
        )

        context.base_lore_text = response

        context.base_lore_data = {
            "generated": True,

            "genre": context.user_requirements.get(
                "genre"
            ),

            "tone": context.user_requirements.get(
                "tone"
            ),

            "magic_level": context.user_requirements.get(
                "magic_level"
            )
        }

        print(
            "[BaseLoreAgent] Completed"
        )

        return context