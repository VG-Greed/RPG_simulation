import os
import asyncio

from django.shortcuts import render

from dotenv import load_dotenv

from llm.openai_client import OpenAIClient

from core.orchestrator import (
    Orchestrator
)


load_dotenv()

api_key = os.getenv(
    "OPENAI_API_KEY"
)

llm_client = OpenAIClient(
    api_key
)

orchestrator = Orchestrator(
    llm_client
)


def index(request):

    return render(
        request,
        "generator/index.html"
    )


def generate_world(request):

    if request.method != "POST":

        return render(
            request,
            "generator/index.html"
        )

    user_prompt = request.POST.get(
        "user_prompt",
        ""
    )

    if not user_prompt:

        return render(
            request,
            "generator/index.html",
            {
                "error": "Введите описание мира"
            }
        )

    result_context = asyncio.run(
        orchestrator.run(user_prompt)
    )

    return render(
        request,
        "generator/result.html",
        {
            "result": result_context
        }
    )