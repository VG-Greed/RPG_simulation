import json
import re


def safe_json_loads(
    text: str
) -> dict:

    if not text:

        return {
            "consistency_score": 0,
            "issues": [
                {
                    "category": "parser",
                    "description": "Empty response",
                    "severity": "high"
                }
            ],
            "summary": "Failed to parse response"
        }

    try:

        return json.loads(text)

    except Exception:

        pass

    # =========================
    # REMOVE MARKDOWN
    # =========================

    cleaned = text.strip()

    cleaned = cleaned.replace(
        "```json",
        ""
    )

    cleaned = cleaned.replace(
        "```",
        ""
    )

    # =========================
    # EXTRACT JSON OBJECT
    # =========================

    match = re.search(
        r"\{.*\}",
        cleaned,
        re.DOTALL
    )

    if match:

        cleaned = match.group(0)

    # =========================
    # SECOND ATTEMPT
    # =========================

    try:

        return json.loads(cleaned)

    except Exception as e:

        print()
        print("[JSON PARSER ERROR]")
        print(e)

        print()
        print("[RAW RESPONSE]")
        print(text)

        return {
            "consistency_score": 0,
            "issues": [
                {
                    "category": "parser",
                    "description": (
                        "Failed to parse "
                        "LLM JSON response"
                    ),
                    "severity": "high"
                }
            ],
            "summary": "Parser failure"
        }