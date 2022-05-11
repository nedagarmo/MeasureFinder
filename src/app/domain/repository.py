from abc import ABC


class Repository(ABC):
    async def get_list(self): ...
