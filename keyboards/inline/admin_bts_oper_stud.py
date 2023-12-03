"""Модуль создания клавиатуры."""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def admin_bts_stud() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры для действий с учениками
    :return: InlineKeyboardMarkup
    """
    ikeyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Просмотреть", callback_data="get_students")],
            [InlineKeyboardButton("Создать", callback_data="add_students")],
            [InlineKeyboardButton("Редактировать", callback_data="edit_students")],
            [
                InlineKeyboardButton(
                    "Изменить пароль", callback_data="edit_pass_students"
                )
            ],
            [InlineKeyboardButton("Удалить", callback_data="delete_students")],
            [
                InlineKeyboardButton(
                    "Заблокироть/разблокировать", callback_data="blocked_students"
                )
            ],
            [InlineKeyboardButton("Вернуться назад", callback_data="main_menu")],
        ]
    )
    return ikeyboard
