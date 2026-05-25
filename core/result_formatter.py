from core.world_context import WorldContext


class ResultFormatter:

    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:

        language = context.user_requirements.get(
            "output_language",
            "russian"
        )

        sections = []

        # =========================
        # META
        # =========================

        meta = [
            "WORLD GENERATION RESULT",
            "",
            f"Genre: {context.user_requirements.get('genre', 'unknown')}",
            f"Tone: {context.user_requirements.get('tone', 'unknown')}",
            f"Magic level: {context.user_requirements.get('magic_level', 'unknown')}",
            f"World scale: {context.user_requirements.get('world_scale', 'unknown')}",
            f"Language: {language}",
            ""
        ]

        sections.extend(meta)

        # =========================
        # LORE
        # =========================

        sections.append("WORLD LORE")
        sections.append(context.base_lore_text or "")
        sections.append("")

        # =========================
        # HISTORY
        # =========================

        sections.append("WORLD HISTORY")
        sections.append(context.history_text or "")
        sections.append("")

        # =========================
        # OPTIONAL PARTS
        # =========================

        if context.geography_text:
            sections.append("GEOGRAPHY")
            sections.append(context.geography_text)
            sections.append("")

        if context.politics_text:
            sections.append("POLITICS")
            sections.append(context.politics_text)
            sections.append("")

        if context.cultures_text:
            sections.append("CULTURES & RELIGIONS")
            sections.append(context.cultures_text)
            sections.append("")

        # =========================
        # CONSISTENCY
        # =========================

        if context.consistency_issues:
            sections.append("CONSISTENCY REPORT")
            score = context.consistency_report.get(
                "consistency_score",
                "unknown"
            )

            sections.append(
                f"Общая оценка согласованности: {score}/10"
            )

            sections.append("")

            for issue in context.consistency_issues:

                category = issue.get(
                    "category",
                    "unknown"
                )

                severity = issue.get(
                    "severity",
                    "unknown"
                )

                description = issue.get(
                    "description",
                    ""
                )

                sections.append(
                    f"- [{severity}] "
                    f"{category}: "
                    f"{description}"
                )

            sections.append("")

        # =========================
        # FINAL OUTPUT
        # =========================

        context.final_text = "\n".join(sections).strip()

        print("[ResultFormatter] Completed")

        return context