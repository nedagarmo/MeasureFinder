import pytest

from src.app.application.engine import SearchEngine


@pytest.fixture
def data_mock():
    return [
        {
            "first_name": "Yi",
            "h_in": "80",
            "h_meters": "2.13",
            "last_name": "Jianlian"
        },
        {
            "first_name": "Nick",
            "h_in": "78",
            "h_meters": "1.98",
            "last_name": "Young"
        },
        {
            "first_name": "Thaddeus",
            "h_in": "80",
            "h_meters": "2.03",
            "last_name": "Young"
        }
    ]


@pytest.fixture
def wrong_data_mock():
    return [
        {
            "first_name": "Yi",
            "h_in": "YY",  # Error is here!
            "h_meters": "2.13",
            "last_name": "Jianlian"
        },
        {
            "first_name": "Nick",
            "h_in": "78",
            "h_meters": "1.98",
            "last_name": "Young"
        }
    ]


@pytest.mark.asyncio
async def test_search_engine_results(data_mock, capfd):
    first_use_case = 160
    second_use_case = 158

    await SearchEngine(height=first_use_case, data=data_mock).handle()
    out, err = capfd.readouterr()
    assert out == "- Thaddeus Young    Yi Jianlian\n"
    await SearchEngine(height=second_use_case, data=data_mock).handle()
    out, err = capfd.readouterr()
    assert out == "- Nick Young        Yi Jianlian\n- Thaddeus Young    Nick Young\n"


@pytest.mark.asyncio
async def test_engine_resilience(wrong_data_mock, capfd):
    first_use_case = 160

    await SearchEngine(height=first_use_case, data=wrong_data_mock).handle()
    out, err = capfd.readouterr()
    assert out == "No matches found\n"
