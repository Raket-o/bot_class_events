"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .back_main_menu import callback_main_menu


def admin_bts_eve() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для модуля 'handlers.custom_handlers.show_history'
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Просмотреть",
                              callback_data='get_events')],
        [InlineKeyboardButton("Создать",
                              callback_data='add_events')],
        [InlineKeyboardButton("Редактировать",
                              callback_data='edit_events')],
        [InlineKeyboardButton("Удалить",
                              callback_data='delete_events')],
    ])
    # ikeyboard.add(callback_main_menu())
    return ikeyboard

