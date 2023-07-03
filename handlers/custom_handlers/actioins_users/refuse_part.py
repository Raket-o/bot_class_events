""" Модуль обработки каллбэка refuse_part"""

from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import UserActionState
from database import database
from keyboards.reply.list_button import list_button


@dp.callback_query_handler(lambda callback_query: callback_query.data == "refuse_part")
async def refuse_part_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функия refuse_part_1. Каллбэк с датой refuse_part запускает данную функцию.
    Проверяет, участвует ли ученик в событии. Если участвует, отменяет заявку.
    Иначе сообщает "Вы не участвовали."
    """
    async with state.proxy() as data:
        id_telegram = data["id_telegram"]
        event = data["event"]

    participation = database.check_participation(id_user=id_telegram, id_event=event[0][0])
    if participation:
        database.del_participation(id_student=id_telegram, id_event=event[0][0])

        await message.message.answer('Вы отказались от участия.')
        await state.finish()

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.message.answer('Выберите событие:', reply_markup=kb)
            await UserActionState.name_event.set()
    else:
        await message.message.answer('Вы не участвовали.')

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.message.answer('Выберите событие:', reply_markup=kb)
            await UserActionState.name_event.set()
