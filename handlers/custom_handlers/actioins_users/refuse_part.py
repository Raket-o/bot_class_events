""" Модуль обработки каллбэка back_to_list_event"""

from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import UserActionState
from database import database
from keyboards.reply.list_button import list_button


@dp.callback_query_handler(lambda callback_query: callback_query.data == "refuse_part")
async def refuse_part_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функия refuse_part_1. Каллбэк с датой back_to_list_event запускает данную функцию.
    Завершает ожидания состояния и возвращает к списку событий.
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


@dp.message_handler(state=UserActionState.comment)
async def refuse_part_2(message: types.Message, state: FSMContext) -> None:
    input_text = message.text
    async with state.proxy() as data:
        id_user = data["id_telegram"]
        event = data["event"]

    if input_text != "0":
        await message.answer('Вы приняли участие. Комментарий записан.')
        database.add_participation(id_user=id_user, id_event=event[0][0], comment=input_text)
        await state.finish()

        list_events = database.gets_events()

        if list_events:
            kb = list_button(list_events)
            await message.answer('Выберите событие:', reply_markup=kb)
            await UserActionState.name_event.set()
        else:
            await message.answer('События ещё не добавлены.')

    else:
        await message.answer('Вы приняли участие.')
        database.add_participation(id_user=id_user, id_event=event[0][0])
        await state.finish()

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.answer('Выберите событие:', reply_markup=kb)
            await UserActionState.name_event.set()
        else:
            await message.answer('События ещё не добавлены.')
