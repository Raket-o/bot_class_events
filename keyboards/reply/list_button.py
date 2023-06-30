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

    # lst_for_button.append("События:")

    # print(lst)
    #
    # for i in lst:
    #     lst_for_button.append(i[3])

    # print(lst_for_button)
    lst.append((0, 0, 0, "Выйти"))

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    # keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


    # keyboard.add(*(KeyboardButton(i_lst[0]) for i_lst in sorted(lst)))
    keyboard.add(*(KeyboardButton(i_lst[3]) for i_lst in lst))

    return keyboard
