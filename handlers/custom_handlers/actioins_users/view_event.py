""" Модуль просмотра события"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline import logout
from keyboards.inline.user_bts_oper_events import user_bts_eve
from loader import dp
from states.states import UserActionState


@dp.message_handler(state=UserActionState.name_event)
async def view_event(message: types.Message, state: FSMContext) -> None:
    """
    Функций view_event. Запрашивает в базе событие по имени и выводит пользователю.
    """
    input_text = message.text
    event = database.get_event_by_name(input_text)
    if input_text == "Выйти":
        kb = logout.logout_bts()
        await message.answer('Действительно хотите выйти?', reply_markup=kb)
        await state.finish()

    if event:
        await state.finish()

        kb = user_bts_eve()
        await message.answer(
            f'Название: {event[0][3]}\n Дата: {event[0][4]}\n Описание: {event[0][5]}',
            reply_markup=kb
        )
        async with state.proxy() as data:
            data["id_telegram"] = message.from_id
            data["event"] = event

    elif not event and input_text != "Выйти":
        await message.answer('Нет информации. Пожалуйста, выберете другое событие.')
