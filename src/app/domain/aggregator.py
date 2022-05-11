from abc import ABC


class Aggregator(ABC):
    async def handle(self): ...
