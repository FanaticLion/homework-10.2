import datetime as dt
import re
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """Функция, которая принимает счет и номер карты и возвращает зашифрованный"""
    # Найти только цифровые символы
    only_numbers = re.findall(r"\d+", card_number)
    if not only_numbers:
        raise ValueError("В строке отсутствуют цифры.")

    str_only_numbers = "".join(only_numbers)
    if "Cчет" in card_number:
        return get_mask_account(str_only_numbers)
    else:
        return get_mask_card_number(str_only_numbers)


def get_date(date_format: str) -> str:
    """Функция изменения формата даты"""
    try:
        date_object = dt.datetime.strptime(date_format[0:10], "%Y %m. %d")
    except ValueError:
        raise ValueError(f"time data '{date_format}' does not match format '%Y %m. %d'")

    date_class_str = date_object.strftime("%d.%m.%Y")
    return date_class_str
