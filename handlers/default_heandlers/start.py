""" Модуль команды /start"""

from aiogram import types

from loader import dp
from states.states import UserInfoState

START_MESSAGE = "<b>Введите фамилию и имя ученика</b>"


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    """
    Вывод тест START_MESSAGE и ожидает изменения состояния
    """
    await message.answer(START_MESSAGE, parse_mode="HTML")
    await UserInfoState.student_name.set()
