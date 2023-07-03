""" Модуль обработки каллбэка edit_events"""

from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import EventEditState
from database import database
from keyboards.inline.admin_bts_oper_events import admin_bts_eve
import datetime


@dp.callback_query_handler(lambda callback_query: callback_query.data == "edit_events")
async def edit_events_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите ИД:')
    await EventEditState.id.set()


@dp.message_handler(state=EventEditState.id)
async def edit_events_2(message: types.Message, state: FSMContext) -> None:
    try:
        id = int(message.text)
        data_event = database.check_event_by_id(id)
        # print(data_event)
        if data_event:
            await message.answer('Новое название или введите цифру 0, чтоб его не изменять.')

            async with state.proxy() as data:
                data["id"] = id
                data["name"] = data_event[3]
                data["deadline"] = data_event[4]
                data["description"] = data_event[5]


            await EventEditState.name.set()

        else:
            await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    except ValueError:
        await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')


@dp.message_handler(state=EventEditState.name)
async def edit_events_3(message: types.Message, state: FSMContext) -> None:
    input_text = message.text.capitalize()

    await message.answer('Новая дата (пример- 01.01.2023) или\n введите цифру 0, чтоб его не изменять.')

    if input_text != "0":
        async with state.proxy() as data:
            data["name"] = input_text
        await EventEditState.deadline.set()
    else:
        await EventEditState.deadline.set()


@dp.message_handler(state=EventEditState.deadline)
async def edit_events_4(message: types.Message, state: FSMContext) -> None:
    input_text = message.text
    if input_text != "0":
        try:
            input_date = datetime.datetime.strptime(message.text, "%d.%m.%Y").date()

            async with state.proxy() as data:
                data["deadline"] = input_date
            await EventEditState.description.set()

            await message.answer('Полное описание с ценами и прочим:')
        except ValueError:
            await message.answer('Введена некорректная дата. НЕ ИЗМЕНЕНО!')

    else:
        await message.answer('Новое описание или или введите цифру 0, чтоб его не изменять')
        await EventEditState.description.set()


@dp.message_handler(state=EventEditState.description)
async def edit_events_5(message: types.Message, state: FSMContext) -> None:
    input_text = message.text

    if input_text != "0":
        async with state.proxy() as data:
            data["description"] = input_text
            database.edit_event_by_id(
                data["id"],
                data["name"],
                data["deadline"],
                data["description"]
            )

        kb = admin_bts_eve()
        await message.answer('Изменения внесены.', reply_markup=kb)
        await state.finish()

    else:
        async with state.proxy() as data:
            database.edit_event_by_id(
                data["id"],
                data["name"],
                data["deadline"],
                data["description"]
            )
        kb = admin_bts_eve()
        await message.answer('Изменения внесены.', reply_markup=kb)
        await state.finish()
