import asyncio

from core.world_context import WorldContext

from agents.user_input_agent import UserInputAgent
from agents.base_lore_agent import BaseLoreAgent
from agents.history_agent import HistoryAgent
from agents.geography_agent import GeographyAgent
from agents.politics_agent import PoliticsAgent
from agents.cultures_agent import CulturesAgent

from core.consistency_analyzer import ConsistencyAnalyzer
from core.result_formatter import ResultFormatter


class Orchestrator:

    def __init__(self, llm_client):

        self.user_input_agent = UserInputAgent(llm_client)
        self.lore_agent = BaseLoreAgent(llm_client)
        self.history_agent = HistoryAgent(llm_client)
        self.geography_agent = GeographyAgent(llm_client)
        self.politics_agent = PoliticsAgent(llm_client)
        self.cultures_agent = CulturesAgent(llm_client)

        self.analyzer = ConsistencyAnalyzer(llm_client)
        self.formatter = ResultFormatter()

        self.max_retries = 1

    async def run(self, user_prompt: str) -> WorldContext:


        context = WorldContext(
            user_prompt=user_prompt
        )


        context = await self.user_input_agent.run(context)


        context = await self.lore_agent.run(context)
        context = await self.history_agent.run(context)
        context = await self.geography_agent.run(context)

        context = await self.politics_agent.run(context)
        context = await self.cultures_agent.run(context)

        context = await self.analyzer.run(
            context
        )

        retry_count = 0

        while retry_count < self.max_retries:

            high_severity_found = any(

                issue.get("severity") == "high"

                for issue in context.consistency_issues
            )

            if not high_severity_found:
                break

            print(
                f"[Self-Healing] "
                f"Retry attempt #{retry_count + 1}"
            )

            context = await self.retry_failed_agents(
                context
            )

            context = await self.analyzer.run(
                context
            )

            retry_count += 1


        context = await self.formatter.run(context)

        return context
    
    async def retry_failed_agents(
        self,
        context: WorldContext
    ) -> WorldContext:

        issues = context.consistency_issues

        retry_categories = set()

        for issue in issues:

            severity = issue.get(
                "severity",
                "low"
            )

            if severity != "high":
                continue

            category = issue.get(
                "category",
                ""
            )

            retry_categories.add(category)

        if "history" in retry_categories:

            print(
                "[Self-Healing] "
                "Retrying HistoryAgent"
            )

            context = await self.history_agent.run(
                context
            )

        if "geography" in retry_categories:

            print(
                "[Self-Healing] "
                "Retrying GeographyAgent"
            )

            context = await self.geography_agent.run(
                context
            )

        if "politics" in retry_categories:

            print(
                "[Self-Healing] "
                "Retrying PoliticsAgent"
            )

            context = await self.politics_agent.run(
                context
            )

        if "cultures" in retry_categories:

            print(
                "[Self-Healing] "
                "Retrying CulturesAgent"
            )

            context = await self.cultures_agent.run(
                context
            )

        return context