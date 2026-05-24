import json


def safe_json_loads(text: str) -> dict:

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        cleaned = text.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned.replace(
                "```json",
                ""
            )

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]

        cleaned = cleaned.strip()

        return json.loads(cleaned)