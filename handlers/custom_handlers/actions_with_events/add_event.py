import datetime
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start
from states.states import EventState
from keyboards.reply.list_button import list_button
from keyboards.inline.admin_bts_oper_events import admin_bts_eve
from database import database
from utils.misc.sending_messages import sending_messages


@dp.callback_query_handler(lambda callback_query: callback_query.data == "add_events")
async def add_event_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите название события:')
    await EventState.name.set()


@dp.message_handler(state=EventState.name)
async def add_event_2(message: types.Message, state: FSMContext) -> None:
    input_text = message.text.capitalize()
    async with state.proxy() as data:
        data["name"] = input_text
    await message.answer('Введите даты окончания\n (пример- 01.01.2023).')
    await EventState.deadline.set()


@dp.message_handler(state=EventState.deadline)
async def add_event_3(message: types.Message, state: FSMContext) -> None:
    try:
        # input_text = message.text
        input_date = datetime.datetime.strptime(message.text, "%d.%m.%Y").date()

        async with state.proxy() as data:
            data["deadline"] = input_date
        await EventState.description.set()

        await message.answer('Полное описание с ценами и прочим:')
    except ValueError:
        await message.answer('Введена некорректная дата.\n (пример- 01.01.2023).')


@dp.message_handler(state=EventState.description)
async def add_event_3(message: types.Message, state: FSMContext) -> None:
    author_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    async with state.proxy() as data:
        data["description"] = message.text
        database.add_event_db(
            author_id=message.from_id,
            author_name=author_name,
            name_event=data["name"],
            deadline=data["deadline"],
            description=data["description"]
        )
        await sending_messages(text_message=f'Добавлено новое событие: <b>{data["name"]}</b>')

    kb = admin_bts_eve()
    await message.answer('Записал.', reply_markup=kb)
    await state.finish()