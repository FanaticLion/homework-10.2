import pytest
from src.widget import mask_account_card, get_date


# Фикстура для генерации тестовых данных для маскирования карт и счетов
@pytest.fixture
def card_and_account_test_data():
    """
    Фикстура с примерами разных данных для тестирования mask_account_card.
    """
    return [
        {"input": "Карта 1234-5678-9012-3456", "expected": "**** **** ****3456", "is_card": True},
        {"input": "Cчет: 12345678", "expected": "**5678", "is_card": False},
        {"input": "Карта ABCD-EFGH", "expected": None, "is_card": True},  # Ошибка (нет цифр)
        {"input": "Cчет: ABCD", "expected": None, "is_card": False},  # Ошибка (нет цифр)
        {"input": "Карта 1234", "expected": None, "is_card": True},  # Короткий номер карты
        {"input": "Cчет: 12", "expected": None, "is_card": False},  # Короткий номер счета
        {"input": "Карта", "expected": None},  # Никаких цифр вообще
    ]


# Фикстура для тестирования разных форматов даты
@pytest.fixture
def date_test_data():
    """
    Фикстура с примерами корректных и некорректных данных для тестирования get_date.
    """
    return [
        {"input": "2023 01. 15", "expected": "15.01.2023"},
        {"input": "2021 12. 31", "expected": "31.12.2021"},
        {"input": "2022 02. 29", "expected": None},  # Некорректная дата
        {"input": "15-01-2023", "expected": None},  # Неверный формат
        {"input": "", "expected": None},  # Пустая строка
        {"input": "2023 01. 15 12:00", "expected": None},  # Дополнительные данные
    ]


# Тесты для mask_account_card
def test_mask_account_card(card_and_account_test_data, mocker):
    """
    Тестирование функции mask_account_card на основе тестовых данных.
    """
    mock_mask_card = mocker.patch('src.masks.get_mask_card_number', return_value="1234 56** ****3456")
    mock_mask_account = mocker.patch('src.masks.get_mask_account', return_value="**5678")

    for data in card_and_account_test_data:
        input_data = data["input"]
        expected = data["expected"]

        if expected is None:
            # Ожидание исключения при ошибочных данных
            with pytest.raises(ValueError):
                mask_account_card(input_data)
        else:
            # Проверка результата
            result = mask_account_card(input_data)

            # Проверка вызова соответствующей функции
            if data.get("is_card"):
                mock_mask_card.assert_called_with("1234567890123456")
            else:
                assert result == expected

                # Проверка вызова соответствующей функции
            if data.get("is_card"):
                mock_mask_card.assert_called_with("1234567890123456")
            else:
                mock_mask_account.assert_called_with("12345678")

    # Проверка количества вызовов моков
    mock_mask_card.assert_called()
    mock_mask_account.assert_called()


# Тесты для get_date
def test_get_date(date_test_data):
    """
    Тестирование функции get_date на основе тестовых данных.
    """
    for data in date_test_data:
        input_date = data["input"]
        expected = data["expected"]

        if expected is None:
            # Ожидание исключения при ошибочных данных
            with pytest.raises(ValueError):
                get_date(input_date)
        else:
            # Проверка результата
            result = get_date(input_date)
            assert result == expected
