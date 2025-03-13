import datetime as dt

def get_mask_card_number(card_number: str) -> str:
    card_str = str(card_number)
    if not card_str.isdigit():
        raise ValueError("Card number must contain only digits.")
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")
    return f"**** **** ****{card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    account_str = str(account_number)
    if not account_str.isdigit():
        raise ValueError("Account number must contain only digits.")
    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")
    return f"**{account_str[-4:]}"

