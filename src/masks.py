def get_mask_card_number(card_number: str) -> str:
    card_str = str(card_number)

    # Проверка на пустую строку
    if not card_str.strip():
        raise ValueError("Card number is empty")

    # Проверка на минимальную длину номера карты
    if len(card_str) < 16:
        raise ValueError("Card number is too short")

    # Проверка на то, что номер карты состоит только из цифр
    if not card_str.isdigit():
        raise ValueError("Card number must contain only digits.")

    # Формирование маски
    return f"{card_str[:4]} {card_str[4:6]} ** **** **** {card_str[-4:]}"

def get_mask_account(account_number: str) -> str:
    account_str = str(account_number)

    # Проверка на то, что строка содержит только цифры
    if not account_str.isdigit():
        raise ValueError("Account number must contain only digits.")

    # Проверка на минимальную длину строки
    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")

    # Формирование маски
    masked_part = "*" * (len(account_str) - 4)  # Звездочки вместо всех символов, кроме последних 4
    visible_part = account_str[-4:]  # Последние 4 символа
    return f"{masked_part}{visible_part}"