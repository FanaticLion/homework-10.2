import pytest
from src.processing import filter_by_state,sort_by_date


@pytest.Mark.parametrize(
    "state, result",
    [("EXECUTED"),[[41428829, 939719570] ("CANCELED", [594226727, 615064591]), ("", []

)]
def test_filter_by_state(static_data: list[dict], state: str, result: list[dict]) -> None: