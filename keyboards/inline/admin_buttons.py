"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


def admin_bts() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для модуля 'handlers.custom_handlers.show_history'
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Список событий",
                              callback_data='operations_events')],
        [InlineKeyboardButton("Список учеников",
                              callback_data='operations_students')]

    ],)

    return ikeyboard
