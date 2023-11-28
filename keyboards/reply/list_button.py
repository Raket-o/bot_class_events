"""Модуль генерации клавиатуры. Имя берётся из входящего списка."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def list_button(lst: list) -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры.
    Принимает на вход список где lst[3]: str - названия кнопок,
    остальные элементы опциональны.
    :return: ReplyKeyboardMarkup
    """
    lst.append((0, 0, 0, "Выйти"))
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    keyboard.add(*(KeyboardButton(i_lst[3]) for i_lst in lst))
    return keyboard
