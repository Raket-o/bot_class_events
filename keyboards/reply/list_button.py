"""Модуль генерации клавиатуры. Имя берётся из входящего списка."""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def list_button(lst: list, lst_for_button: list = list()) -> ReplyKeyboardMarkup:
    """
    Функция создания клавиатуры.
    Принимает на вход обязательно список где lst[0]: str - будут названия кнопок,
    остальные элементы опциональны.
    :return: ReplyKeyboardMarkup
    """
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    lst_for_button.append("События:")

    for i in lst:
        lst_for_button.append(i[3])

    print(lst_for_button)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)

    # keyboard.add(*(KeyboardButton(i_lst[0]) for i_lst in sorted(lst)))
    keyboard.add(*(KeyboardButton(i_lst) for i_lst in lst_for_button))

    return keyboard
