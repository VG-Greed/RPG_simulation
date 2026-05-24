from openai import AsyncOpenAI

from llm.base_llm_client import BaseLLMClient


class OpenAIClient(BaseLLMClient):

    def __init__(self, api_key: str):

        self.client = AsyncOpenAI(
            api_key=api_key
        )

    async def generate(
        self,
        prompt: str
    ) -> str:

        response = await self.client.chat.completions.create(
            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional "
                        "worldbuilding assistant."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.8
        )

        return response.choices[0].message.content
