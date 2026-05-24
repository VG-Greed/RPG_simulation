from core.world_context import WorldContext


class ConsistencyAnalyzer:

    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:

        issues = []

        # 1. CHECK LORE EXISTS
        if not context.base_lore_text:
            issues.append(
                "Base lore is missing"
            )

        # 2. CHECK HISTORY EXISTS
        if not context.history_text:
            issues.append(
                "History is missing"
            )

        # 3. MIN LENGTH CHECK
        if len(context.base_lore_text) < 300:
            issues.append(
                "Base lore is too short"
            )

        if len(context.history_text) < 300:
            issues.append(
                "History is too short"
            )

        # 4. SIMPLE CONSISTENCY CHECK      
        lore = context.base_lore_text.lower()
        history = context.history_text.lower()

        # example heuristic: shared key terms
        key_terms = [
            "magic",
            "war",
            "empire",
            "kingdom",
            "god",
            "ancient"
        ]

        missing_links = []

        for term in key_terms:

            if term in lore and term not in history:
                missing_links.append(term)

        if len(missing_links) > 3:
            issues.append(
                f"Possible inconsistency: missing concepts in history: {missing_links}"
            )

        # SAVE RESULTS
        context.consistency_issues = issues

        print(
            "[ConsistencyAnalyzer] Completed"
        )

        return context