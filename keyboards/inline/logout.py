from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def logout_bts() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для модуля 'handlers.custom_handlers.show_history'
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Перезапустить",
                              callback_data='logout')]
    ])
    return ikeyboard
