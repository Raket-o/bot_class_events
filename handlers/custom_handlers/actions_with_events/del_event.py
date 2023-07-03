""" Модуль обработки каллбэка delete_events"""

from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import EventDelState
from database import database
from keyboards.inline.admin_bts_oper_events import admin_bts_eve


@dp.callback_query_handler(lambda callback_query: callback_query.data == "delete_events")
async def del_event_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функия del_event_1. Каллбэк с датой delete_events запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer('Введите ИД:')
    await EventDelState.id.set()


@dp.message_handler(state=EventDelState.id)
async def del_event_2(message: types.Message, state: FSMContext) -> None:
    """
    Функия del_event_2. Проверяет, существует ли событие по ИД и удаляет его.
    """
    try:
        id = int(message.text)
        data_user = database.check_event_by_id(id)
        if data_user:
            database.del_event_by_id(id)
            kb = admin_bts_eve()
            await message.answer('Событие удалённо.', reply_markup=kb)
            await state.finish()
        else:
            await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    except ValueError:
        await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')
