import pytest
from src.processing import filter_by_state,sort_by_date


@pytest.mark.parametrize(
    "state, result",
    [("EXECUTED", [41428829, 939719570]),("CANCELED", [594226727, 615064591]), ("", []),])
def test_filter_by_state(static_data: list[dict], state: str, result: list[int]) -> None:
    filtered_transactive = filter_by_state(static_data, state)
    filtered_ids = [transactive['id'] for transactive in filtered_transactive]
    assert filtered_ids == result

@pytest.mark.parametrize(
    "data, result",
    [
         (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    ],
            )
        ],
    )
def test_sort_by_date(data: list[dict], result: list[dict]) -> None:
    sorted_data = sort_by_date(data)
    assert sorted_data == result
