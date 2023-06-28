"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .back_main_menu import callback_main_menu


def admin_bts_stud() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для модуля 'handlers.custom_handlers.show_history'
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Просмотреть",
                              callback_data='get_students')],
        [InlineKeyboardButton("Создать",
                              callback_data='add_students')],
        [InlineKeyboardButton("Редактировать",
                              callback_data='edit_students')],
        [InlineKeyboardButton("Удалить",
                              callback_data='delete_students')],
        [InlineKeyboardButton("Заблокироть/разблокировать",
                              callback_data='delete_students')],
        [InlineKeyboardButton("Вернуться назад",
                              callback_data='main_menu')],
    ], one_time_keyboard=True)
    # ikeyboard.add(callback_main_menu())
    return ikeyboard

