import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    """Функция тестирования масок карт"""

    # Тесты на корректное поведение функции
    assert get_mask_card_number("21541221421212525845") == "2154 12 ** **** **** 5845"
    assert get_mask_card_number("12341234123412345678") == "1234 12 ** **** **** 5678"

    # Тестирование исключений
    with pytest.raises(ValueError, match="Card number is too short"):
        get_mask_card_number("215412214212125")  # Слишком короткий номер

    with pytest.raises(ValueError, match="Card number is empty"):
        get_mask_card_number("")  # Пустая строка


def test_get_mask_account() -> None:
    """Функция тестирования масок счетов"""

    # Тесты на корректное поведение функции
    assert get_mask_account("12345678901234567890") == "****567890"
    assert get_mask_account("98765432109876543210") == "****432110"

    # Тестирование исключений
    with pytest.raises(ValueError, match="Account number is too short"):
        get_mask_account("12345")  # Слишком короткий номер

    with pytest.raises(ValueError, match="Account number is empty"):
        get_mask_account("")  # Пустая строка


