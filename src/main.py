import asyncio

from app.application.engine import SearchEngine
from config import PLAYERS_SERVICE_URL
from app.infrastructure.repositories.players import PlayersRepository


async def launch_interactivity(players: list):
    """
    Function responsible for launching messages to the console to interact with the user and run the aggregator.
    :param players: data source list
    """
    print("\nPlease type a height to find the pairs: ")
    height = int(input())
    await SearchEngine(height=height, data=players).handle()


async def startup():
    """
    Function responsible for starting the application and loading the list of players from the data source.
    """
    print("Welcome!")
    players = await PlayersRepository(url=PLAYERS_SERVICE_URL).get_list()
    if len(players) > 0:
        while True:
            try:
                await launch_interactivity(players)
            except ValueError as err:
                print("Write an integer as height.\n")

    print("Failed to load player list.")

if "__main__" == __name__:
    asyncio.run(startup())
