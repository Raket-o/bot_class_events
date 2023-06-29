import logging
from aiogram import types
from loader import dp
from states.states import UserInfoState, AdminInfoState
from aiogram.dispatcher import FSMContext
from database import database

from keyboards import reply
from keyboards.inline import admin_buttons
from keyboards.reply.list_button import list_button
from keyboards.inline import logout




@dp.message_handler(state=UserInfoState.student_name)
async def input_name(message: types.Message, state: FSMContext) -> None:
    input_text_user = message.text.title()

    if database.check_users(input_text_user):
        async with state.proxy() as data:
            data["name"] = input_text_user

        await message.answer('Введите пароль.')
        await UserInfoState.password.set()

    else:
        await message.answer('Такой ученик не найден.')


@dp.message_handler(state=UserInfoState.password)
async def input_password(message: types.Message, state: FSMContext) -> None:
    input_text_user = message.text

    async with state.proxy() as data:
        name_user = data["name"]

    if database.check_password(name_user, input_text_user):
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

        if list_events:
            kb = reply.list_button(list_events)
            await message.answer('Текущие события:', reply_markup=kb)
        else:
            await message.answer('Событий нет.')

        if input_text_user[0] == "1":
            print("Login 'admin'")
            kb = admin_buttons.admin_bts()
            await message.answer('Админ меню:', reply_markup=kb)
        await state.finish()

    else:
        await state.finish()
        kb = logout.logout_bts()
        await message.answer('Не правильный пароль.', reply_markup=kb)






# @dp.message_handler(state=UserInfoState.student_name)
# async def input_name(message: types.Message, state: FSMContext) -> None:
#     pass
#
#
# @dp.message_handler(state=UserInfoState.student_name)
# async def input_password(message: types.Message, state: FSMContext) -> None:
#     input_text_user = message.text.title().split()
#     try:
#         id_student, *_ = database.check_password(input_text_user)
#     except TypeError:
#         pass
#
#     if database.check_password(input_text_user):
#         user_id = message.from_id
#         user_first_name = message.from_user.first_name
#         user_last_name = message.from_user.last_name
#
#         database.update_info_for_db(
#             telegram_id=user_id,
#             user_first_name=user_first_name,
#             user_last_name=user_last_name,
#             student_name=input_text_user[0]
#         )
#
#         list_events = database.get_evets()
#
#         if list_events:
#             kb = reply.list_button(list_events)
#             await message.answer('Текущие события:', reply_markup = kb)
#         else:
#             await message.answer('событий нет.')
#
#         if input_text_user[0] == "Admin":
#             print("Login 'admin'")
#             kb = admin_buttons.admin_bts()
#             await message.answer('Админ меню:', reply_markup = kb)
#
#             # kb = list_button(("События", "Ученики", "Выйти"))
#
#             # await message.answer('Админ меню:', reply_markup = kb)
#             # await AdminInfoState.change_eve_st.set()
#
#         await state.finish()
#
#     else:
#         await message.answer('Такой ученик не найден. Или не правильный пароль. ')
