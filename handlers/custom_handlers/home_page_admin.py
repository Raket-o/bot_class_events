
import logging
from aiogram import types
from loader import dp
from states.states import UserInfoState
from aiogram.dispatcher import FSMContext
from database import database

from keyboards.inline import main_menu


@dp.message_handler(state=UserInfoState.student_name)
async def get_met_sort_low(message: types.Message, state: FSMContext) -> None:
    input_text_user = message.text.title().split()
    try:
        id_student, *_ = database.check_password(input_text_user)
    except TypeError:
        pass
    if database.check_password(input_text_user):
        user_id = message.from_id
        user_first_name = message.from_user.first_name
        user_last_name = message.from_user.last_name

        database.update_info_for_db(
            telegram_id=user_id,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            id_student=id_student
        )



        print("ok")
    else:
        await message.answer('Такой ученик не найден. Или не правильный пароль. ')



