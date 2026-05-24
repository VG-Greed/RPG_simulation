from openai import AsyncOpenAI

from llm.base_llm_client import BaseLLMClient


class OpenAIClient(BaseLLMClient):

    def __init__(
        self,
        api_key: str
    ):

        self.client = AsyncOpenAI(
            api_key=api_key
        )

    async def generate(
        self,
        prompt: str,
        *,
        system_prompt: str = (
            "You are a professional "
            "worldbuilding assistant."
        ),
        model: str = "gpt-4.1-mini",
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> str:

        response = await self.client.chat.completions.create(
            model=model,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=temperature,

            max_tokens=max_tokens
        )

        return response.choices[0].message.content
    