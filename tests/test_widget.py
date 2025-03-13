import pytest
from src.widget import get_date, mask_account_card
from src.masks import get_mask_account

# Фикстура для генерации тестовых данных словаря и списка
@pytest.fixture
def account_test_data():
    """
    Фикстура, предоставляющая словарь и список тестовых данных для счета.
    """
    return {
        "valid_accounts": [
            "12345678901234567890",  # стандартный случай
            "11111111111111111111",
        ],
        "short_accounts": ["12345", "12"],  # короткие счета
        "empty": [""],  # пустые строки
    }


@pytest.fixture
def date_test_data():
    """
    Фикстура, предоставляющая список дат с различными форматами.
    """
    return [
        {"input": "2023 01. 15", "expected_output": "15.01.2023"},
        {"input": "2021 12. 31", "expected_output": "31.12.2021"},
        {"input": "2022 02. 29", "expected_output": None},  # Некорректная дата
        {"input": "15-01-2023", "expected_output": None},  # Неверный формат
        {"input": "", "expected_output": None},  # Пустая строка
    ]


# Тесты для get_mask_account
def test_get_mask_account_valid_states(account_test_data):
    """Тестирование корректных состояний функции get_mask_account."""
    for account in account_test_data["valid_accounts"]:
        assert get_mask_account(account) == f"****{account[-6:]}"


def test_get_mask_account_with_invalid_data(account_test_data):
    """
    Тестирование исключений в случае с коротким счетом или пустыми данными.
    """
    for account in account_test_data["short_accounts"]:
        with pytest.raises(ValueError, match="Account number is too short"):
            get_mask_account(account)

    for account in account_test_data["empty"]:
        with pytest.raises(ValueError, match="Account number is empty"):
            get_mask_account(account)


# Тесты для get_date
def test_get_date_valid_formats(date_test_data):
    """Тестирование корректных форматов даты."""
    for test_case in date_test_data:
        input_date = test_case["input"]
        expected_output = test_case["expected_output"]

        if expected_output is not None:
            assert get_date(input_date) == expected_output
        else:
            with pytest.raises(ValueError):
                get_date(input_date)


def test_get_date_edge_case():
    """Дополнительный тест на случай лишних данных в формате даты."""
    with pytest.raises(ValueError, match="unconverted data remains:"):
        get_date("2023 01. 15 00:00")

# Моки для функций из src.masks
@pytest.fixture
def mock_get_mask_account(mocker):
    return mocker.patch('src.masks.get_mask_account', return_value="****1234")


@pytest.fixture
def mock_get_mask_card_number(mocker):
    return mocker.patch('src.masks.get_mask_card_number', return_value="****5678")


# Тесты для get_date
def test_get_date_valid_format():
    input_date = "2023 01. 15"
    expected_output = "15.01.2023"
    assert get_date(input_date) == expected_output


def test_get_date_invalid_format():
    input_date = "15-01-2023"  # Некорректный формат
    with pytest.raises(ValueError, match="time data '15-01-2023' does not match format '%Y %m. %d'"):
        get_date(input_date)


# Тесты для mask_account_card
def test_mask_account_card_account(mock_get_mask_account):
    input_card = "Cчет 12345678"
    expected_output = "****1234"  # Мок возвращае эту строку
    assert mask_account_card(input_card) == expected_output
    mock_get_mask_account.assert_called_once_with("12345678")


def test_mask_account_card_card_number(mock_get_mask_card_number):
    input_card = "Карта 43215678"
    expected_output = "****5678"  # Мок возвращае эту строку
    assert mask_account_card(input_card) == expected_output
    mock_get_mask_card_number.assert_called_once_with("43215678")


def test_mask_account_card_no_numbers():
    input_card = "Карта ABCD"
    with pytest.raises(ValueError, match="No digits found in card_number"):
        mask_account_card(input_card)