""" Модуль home_page. Распределяет доступ к админ меню и клиента."""

import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from config_data.config import ADMIN_LOG, ADMIN_PASS
from database import database
from keyboards import reply
from keyboards.inline import admin_buttons, logout
from loader import dp
from states.states import UserActionState, UserInfoState

logger = logging.getLogger("logger_loader")


@dp.message_handler(state=UserInfoState.student_name)
async def input_name(message: types.Message, state: FSMContext) -> None:
    """
    Функция input_name. Делает запрос по ФИ, если проверка пройдена,
    ожидает ввод пароля.
    """
    input_text_user = message.text.title()

    if database.check_users(input_text_user):
        async with state.proxy() as data:
            data["name"] = input_text_user

        await message.answer("Введите пароль.")
        await UserInfoState.password.set()

    else:
        await message.answer("Такой ученик не найден.")


@dp.message_handler(state=UserInfoState.password)
async def input_password(message: types.Message, state: FSMContext) -> None:
    """
    Функция input_password. Проверяет валидность пароля.
    Распределяет обязанности (admin, user)
    """
    input_text_user = message.text

    async with state.proxy() as data:
        student_name = data["name"]

    if database.check_password(student_name, input_text_user):
        user_id = message.from_id
        user_first_name = message.from_user.first_name
        user_last_name = message.from_user.last_name

        database.update_info_for_db(
            telegram_id=user_id,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            student_name=student_name,
        )
        await state.finish()

        if student_name == ADMIN_LOG and input_text_user == ADMIN_PASS:
            logger.info(f"Login 'admin: {student_name}'")
            kb = admin_buttons.admin_bts()
            await message.answer("Админ меню:", reply_markup=kb)
        else:
            logger.info(f"Login 'user: {student_name}'")
            list_events = database.gets_events()

            if list_events:
                kb = reply.list_button.list_button(list_events)
                await message.answer("Выберите событие:", reply_markup=kb)
                await UserActionState.name_event.set()
            else:
                await message.answer("События ещё не добавлены.")

    else:
        await state.finish()
        kb = logout.logout_bts()
        await message.answer("Не правильный пароль.", reply_markup=kb)
