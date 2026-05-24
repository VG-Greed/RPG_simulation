USER_INPUT_PROMPT = """
Analyze the user's world description.

Extract structured worldbuilding information.

Return ONLY valid JSON.

User description:
{user_prompt}

JSON schema:
{{
    "genre": "",
    "tone": "",
    "magic_level": "",
    "technology_level": "",
    "world_scale": "",
    "output_language": "",
    "themes": []
}}

Rules:
- themes must be an array
- detect desired output language
- return valid JSON only
- do not include explanations
"""