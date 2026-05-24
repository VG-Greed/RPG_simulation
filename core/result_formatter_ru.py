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
        # МЕТА-ИНФОРМАЦИЯ
        # =========================

        meta = [
            "РЕЗУЛЬТАТ ГЕНЕРАЦИИ МИРА",
            "",
            f"Жанр: {context.user_requirements.get('genre', 'не указан')}",
            f"Тон: {context.user_requirements.get('tone', 'не указан')}",
            f"Уровень магии: {context.user_requirements.get('magic_level', 'не указан')}",
            f"Масштаб мира: {context.user_requirements.get('world_scale', 'не указан')}",
            f"Язык вывода: {language}",
            ""
        ]

        sections.extend(meta)

        # =========================
        # ЛОР МИРА
        # =========================

        sections.append("ЛОР МИРА")
        sections.append(context.base_lore_text or "")
        sections.append("")

        # =========================
        # ИСТОРИЯ МИРА
        # =========================

        sections.append("ИСТОРИЯ МИРА")
        sections.append(context.history_text or "")
        sections.append("")

        # =========================
        # ДОПОЛНИТЕЛЬНЫЕ РАЗДЕЛЫ
        # =========================

        if context.geography_text:
            sections.append("ГЕОГРАФИЯ")
            sections.append(context.geography_text)
            sections.append("")

        if context.politics_text:
            sections.append("ПОЛИТИЧЕСКАЯ СТРУКТУРА")
            sections.append(context.politics_text)
            sections.append("")

        if context.cultures_text:
            sections.append("КУЛЬТУРЫ И РЕЛИГИИ")
            sections.append(context.cultures_text)
            sections.append("")

        # =========================
        # ОТЧЁТ О СОГЛАСОВАННОСТИ
        # =========================

        if context.consistency_issues:
            sections.append("ОТЧЁТ О СОГЛАСОВАННОСТИ")

            for issue in context.consistency_issues:
                sections.append(f"- {issue}")

            sections.append("")

        # =========================
        # ФИНАЛЬНЫЙ РЕЗУЛЬТАТ
        # =========================

        context.final_text = "\n".join(sections).strip()

        print("[ResultFormatter] Completed")

        return context