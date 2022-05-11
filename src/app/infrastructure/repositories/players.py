from typing import Optional

import aiohttp

from ...domain.repository import Repository


class PlayersRepository(Repository):
    def __init__(self, url: str):
        self._url = url

    async def get_list(self) -> Optional[list[dict]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["values"]
