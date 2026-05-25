from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class WorldContext:

    # USER INPUT
    user_prompt: str = ""

    user_requirements: Dict[str, Any] = field(
        default_factory=dict
    )

    # BASE LORE
    base_lore_data: Dict[str, Any] = field(
        default_factory=dict
    )

    base_lore_text: str = ""

    # HISTORY
    history_data: List[Dict[str, Any]] = field(
        default_factory=list
    )

    history_text: str = ""

    # OPTIONAL AGENTS
    geography_data: Dict[str, Any] = field(
        default_factory=dict
    )

    geography_text: str = ""

    regions_data: List[Dict[str, Any]] = field(
        default_factory=list
    )

    regions_text: str = ""

    settlements_data: List[Dict[str, Any]] = field(
        default_factory=list
    )

    settlements_text: str = ""

    politics_data: Dict[str, Any] = field(
        default_factory=dict
    )

    politics_text: str = ""

    cultures_data: List[Dict[str, Any]] = field(
        default_factory=list
    )

    cultures_text: str = ""

    religions_data: List[Dict[str, Any]] = field(
        default_factory=list
    )

    religions_text: str = ""

    # ANALYSIS

    consistency_report: Dict[str, Any] = field(
        default_factory=dict
    )

    consistency_issues: List[Dict[str, Any]] = field(
        default_factory=list
    )

    validation_results: Dict[str, Any] = field(
        default_factory=dict
    )

    # FINAL RESULT
    final_text: str = ""

    def debug_print(self):

        print()
        print("WORLD CONTEXT")
        print()

        print("USER REQUIREMENTS:")
        print(self.user_requirements)

        print()
        print("BASE LORE:")
        print(self.base_lore_text[:500])

        print()
        print("HISTORY:")
        print(self.history_text[:500])

        print()
        print("GEOGRAPHY:")
        print(self.geography_text[:300])

        print()
        print("POLITICS:")
        print(self.politics_text[:300])

        print()
        print("CULTURES:")
        print(self.cultures_text[:300])

        print()
        print("CONSISTENCY REPORT:")
        print(self.consistency_report)