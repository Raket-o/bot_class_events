from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def logout_bts() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для релогина
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Перезапустить", callback_data="logout")]
        ]
    )
    return ikeyboard
