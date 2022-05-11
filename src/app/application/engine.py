from ..domain.aggregator import Aggregator


class SearchEngine(Aggregator):
    """
    Aggregator class in charge of searching for pairs of players whose added height results
    in the number provided by the user.
    """
    def __init__(self, height: int, data: list):
        self._height = height
        self._data = data

    async def handle(self):
        history = list()  # History list to save verified players and avoid a quadratic complexity of the algorithm
        found = False

        for player in self._data:
            try:
                h_in_parsed = int(player["h_in"])
            except ValueError as _:
                continue

            searched_height = self._height - h_in_parsed
            try:
                i = history.index(searched_height)  # if the element is not found in the list, the exception is fired
                print(f"- {player['first_name']} {player['last_name']}".ljust(20) +
                      f"{self._data[i]['first_name']} {self._data[i]['last_name']}")
                found = True
            except ValueError as _:
                ...

            history.append(h_in_parsed)

        if not found:
            print("No matches found")
