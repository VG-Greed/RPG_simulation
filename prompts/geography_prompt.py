GEOGRAPHY_PROMPT = """
Generate the geography of a tabletop RPG world.

Output language:
{language}

World lore:
{base_lore}

World history:
{history}

Requirements:
- Do not introduce magical geography unless explicitly requested.
- describe continents or major regions
- describe climate and environment
- include mountains, forests, rivers, seas, wastelands, or other natural features
- maintain consistency with lore and history
- support immersive worldbuilding
- suitable for tabletop RPG campaigns
- 1000-2500 characters

The geography should include:
- major landmasses
- dangerous locations
- climate zones
- unique natural phenomena

Return plain text only.
"""