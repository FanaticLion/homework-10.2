import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number() -> None:

    '''Функция тестирования масок карт'''

assert get_mask_card_number("21541221421212525845") == "2154 12 ** **** **** 5845"
with pytest.raises(ValueError):
    get_mask_card_number("215412214212125")

with pytest.raises(ValueError):
    get_mask_card_number("")