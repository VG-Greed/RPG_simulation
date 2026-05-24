from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class WorldContext:
    user_requirements: Dict[str, Any] = field(default_factory=dict)

    base_lore: Dict[str, Any] = field(default_factory=dict)

    geography: Dict[str, Any] = field(default_factory=dict)

    regions: List[Dict[str, Any]] = field(default_factory=list)

    settlements: List[Dict[str, Any]] = field(default_factory=list)

    history: List[Dict[str, Any]] = field(default_factory=list)

    politics: Dict[str, Any] = field(default_factory=dict)

    cultures: List[Dict[str, Any]] = field(default_factory=list)

    consistency_issues: List[str] = field(default_factory=list)