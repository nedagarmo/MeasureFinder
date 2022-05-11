import pytest

from src.app.infrastructure.repositories.players import PlayersRepository
from src.config import PLAYERS_SERVICE_URL


@pytest.mark.asyncio
async def test_get_players():
    results = await PlayersRepository(url=PLAYERS_SERVICE_URL).get_list()
    assert isinstance(results, list)
    assert len(results) > 0
