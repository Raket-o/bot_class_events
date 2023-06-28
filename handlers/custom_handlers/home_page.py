import logging
from aiogram import types
from loader import dp
from states.states import UserInfoState, AdminInfoState
from aiogram.dispatcher import FSMContext
from database import database

from keyboards import reply
from keyboards.inline import admin_buttons
from keyboards.reply.list_button import list_button


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
            student_name=input_text_user[0]
        )

        list_events = database.get_evets()

        # await state.finish()

        # await message.answer('Текущие события:')
        if list_events:
            kb = reply.list_button(list_events)
            await message.answer('Текущие события:', reply_markup = kb)
        else:
            await message.answer('событий нет.')

        if input_text_user[0] == "Admin":
            print("Login 'admin'")
            # kb = admin_buttons.admin_bts()

            kb = admin_buttons.admin_bts()
            await message.answer('Админ меню:', reply_markup = kb)

            # kb = list_button(("События", "Ученики", "Выйти"))

            # await message.answer('Админ меню:', reply_markup = kb)
            # await AdminInfoState.change_eve_st.set()


        await state.finish()


    else:
        await message.answer('Такой ученик не найден. Или не правильный пароль. ')
