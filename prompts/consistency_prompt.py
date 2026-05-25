CONSISTENCY_PROMPT = """
Analyze the consistency of a tabletop RPG world.

Output language:
{language}

WORLD LORE:
{base_lore}

WORLD HISTORY:
{history}

WORLD GEOGRAPHY:
{geography}

WORLD POLITICS:
{politics}

WORLD CULTURES:
{cultures}

Your task:
- identify logical contradictions
- identify timeline inconsistencies
- identify geography inconsistencies
- identify political inconsistencies
- identify cultural inconsistencies
- evaluate overall coherence

Return ONLY valid JSON.

JSON schema:
{{
    "consistency_score": 0,
    "issues": [
        {{
            "category": "",
            "description": "",
            "severity": ""
        }}
    ],
    "summary": ""
}}

Rules:
- consistency_score must be from 1 to 10
- severity must be:
  low / medium / high
- if no issues found, return empty array
- return valid JSON only
"""