def get_mask_card_number(card_number: str) -> str:
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")


def get_mask_account(account_number: str) -> str:
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")