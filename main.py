"""import asyncio
import os

from dotenv import load_dotenv

from llm.openai_client import OpenAIClient
from core.orchestrator import Orchestrator


load_dotenv()


async def main():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing")

    llm_client = OpenAIClient(api_key)

    orchestrator = Orchestrator(llm_client)

    print("\n=== WORLD GENERATION STARTED ===\n")

    user_input = input(
        "Describe your world:\n> "
    )

    result_context = await orchestrator.run(user_input)

    print("\n\n=== FINAL RESULT ===\n")
    print(result_context.final_text)


if __name__ == "__main__":
    asyncio.run(main())"""

from ui.app import app


if __name__ == "__main__":

    app.run(
        debug=True
    )