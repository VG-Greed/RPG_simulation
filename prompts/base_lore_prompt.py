BASE_LORE_PROMPT = """
Generate a fictional world description.

Output language:
{language}

User requirements:
{requirements}

User original description:
{user_prompt}

IMPORTANT RULES:
- strictly follow the user request
- do not introduce magic unless explicitly requested
- do not introduce fantasy races unless explicitly requested
- do not introduce medieval kingdoms unless appropriate
- preserve the requested genre and tone
- if the setting is realistic or modern, maintain realism
- supernatural elements should only appear if requested
- focus on the themes described by the user

Requirements:
- immersive worldbuilding
- coherent setting
- suitable for storytelling or tabletop RPG use
- 1000-3000 characters

Return plain text only.
"""