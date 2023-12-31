"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def admin_bts() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для главного админ меню
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Список событий", callback_data="operations_events")],
            [
                InlineKeyboardButton(
                    "Список учеников", callback_data="operations_students"
                )
            ],
            [
                InlineKeyboardButton(
                    "Сделать общую рассылку", callback_data="all_sending_message"
                )
            ],
            [InlineKeyboardButton("Выйти", callback_data="logout")],
        ],
    )
    return ikeyboard
