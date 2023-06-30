"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_bts_eve() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для модуля 'handlers.custom_handlers.show_history'
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                "Принять участие",
                callback_data='take_part')
            ],
            [InlineKeyboardButton(
                "Отказаться от участия",
                callback_data='refuse_part')
            ],
            [InlineKeyboardButton(
                "Вернуться назад", callback_data='back_to_list_event')
            ]
        ]
    )
    return ikeyboard
