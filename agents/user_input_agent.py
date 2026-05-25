from agents.base_agent import BaseAgent

from core.world_context import WorldContext
from core.json_parser import safe_json_loads

from llm.base_llm_client import BaseLLMClient

from agents.prompts.user_input_prompt import (
    USER_INPUT_PROMPT
)


class UserInputAgent(BaseAgent):

    def __init__(
        self,
        llm_client: BaseLLMClient
    ):

        self.llm_client = llm_client

    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:

        prompt = USER_INPUT_PROMPT.format(
            user_prompt=context.user_prompt
        )

        response = await self.llm_client.generate(
            prompt=prompt,

            system_prompt=(
                "You extract structured "
                "worldbuilding parameters."
            ),

            model="gpt-4.1-nano",

            temperature=0.2,

            max_tokens=500
        )

        parsed_data = safe_json_loads(
            response
        )

        context.user_requirements = {

            "genre": parsed_data.get(
                "genre",
                "fantasy"
            ),

            "tone": parsed_data.get(
                "tone",
                "neutral"
            ),

            "magic_level": parsed_data.get(
                "magic_level",
                "medium"
            ),

            "technology_level": parsed_data.get(
                "technology_level",
                "medieval"
            ),

            "world_scale": parsed_data.get(
                "world_scale",
                "regional"
            ),

            "output_language": parsed_data.get(
                "output_language",
                "russian"
            ),

            "themes": parsed_data.get(
                "themes",
                []
            )
        }

        print(
            "[UserInputAgent] Completed"
        )

        return context