""" Модуль обработки каллбэка back_to_list_event"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.reply.list_button import list_button
from loader import dp
from states.states import UserActionState


@dp.callback_query_handler(lambda callback_query: callback_query.data == "back_to_list_event")
async def take_part_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функция take_part_1. Каллбэк с датой back_to_list_event запускает данную функцию.
    Завершает ожидания состояния и возвращает к списку событий.
    """
    await state.finish()
    list_events = database.gets_events()
    if list_events:
        kb = list_button(list_events)
        await message.message.answer('Выберите событие:', reply_markup=kb)
        await UserActionState.name_event.set()
