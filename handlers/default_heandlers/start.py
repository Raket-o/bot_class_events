from aiogram import types
from loader import dp
from states.states import UserInfoState


START_MESSAGE = "<b>Введите фамилию и имя ученика</b>"


@dp.message_handler(commands=["start"])
async def stars_command(message: types.Message) -> None:
    await message.answer(START_MESSAGE, parse_mode="HTML")
    await UserInfoState.student_name.set()
