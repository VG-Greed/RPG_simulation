from abc import ABC, abstractmethod
from core.world_context import WorldContext


class BaseAgent(ABC):

    @abstractmethod
    async def run(
        self,
        context: WorldContext
    ) -> WorldContext:
        pass
