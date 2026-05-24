HISTORY_PROMPT = """
Generate a historical timeline for a tabletop RPG world.

Output language:
{language}

World lore:
{base_lore}

Requirements:
- create at least 5 major historical events
- maintain chronological consistency
- establish cause-effect relationships
- ensure thematic consistency with the lore
- include rise and fall of civilizations if appropriate
- include conflicts, disasters, discoveries, or wars
- maintain immersive storytelling
- 1000-3000 characters

The history should include:
- ancient period
- major turning points
- recent state of the world

Return plain text only.
"""