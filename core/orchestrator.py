import asyncio

from core.world_context import WorldContext

from agents.user_input_agent import UserInputAgent
from agents.base_lore_agent import BaseLoreAgent
from agents.history_agent import HistoryAgent

from core.consistency_analyzer import ConsistencyAnalyzer
from core.result_formatter import ResultFormatter


class Orchestrator:

    def __init__(self, llm_client):

        # =========================
        # AGENTS INITIALIZATION
        # =========================

        self.user_input_agent = UserInputAgent(llm_client)
        self.lore_agent = BaseLoreAgent(llm_client)
        self.history_agent = HistoryAgent(llm_client)

        self.analyzer = ConsistencyAnalyzer()
        self.formatter = ResultFormatter()

    async def run(self, user_prompt: str) -> WorldContext:

        # =========================
        # INIT CONTEXT
        # =========================

        context = WorldContext(
            user_prompt=user_prompt
        )

        # =========================
        # 1. USER INPUT PARSING
        # =========================

        context = await self.user_input_agent.run(context)

        # =========================
        # 2. CORE GENERATION PIPELINE
        # =========================

        context = await self.lore_agent.run(context)
        context = await self.history_agent.run(context)

        # =========================
        # 3. CONSISTENCY CHECK
        # =========================

        context = await self.analyzer.run(context)

        # =========================
        # 4. FINAL FORMATTING
        # =========================

        context = await self.formatter.run(context)

        return context