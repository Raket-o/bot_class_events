""" Модуль обработки каллбэка take_part"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.reply.list_button import list_button
from loader import dp
from states.states import UserActionState


@dp.callback_query_handler(lambda callback_query: callback_query.data == "take_part")
async def take_part_1(
    message: [types.CallbackQuery, types.Message], state: FSMContext
) -> None:
    """
    Функция refuse_part_1. Каллбэк с датой refuse_part запускает данную функцию.
    Проверяет, участвует ли ученик в событии. Если участвует,
    сообщает "Вы уже приняли участие.". Иначе ожидает комментарий.
    """
    async with state.proxy() as data:
        id_telegram = data["id_telegram"]
        event = data["event"]
    participation = database.check_participation(
        id_user=id_telegram, id_event=event[0][0]
    )
    if participation:
        await message.message.answer("Вы уже приняли участие.")
        await state.finish()

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.message.answer("Выберите событие:", reply_markup=kb)
            await UserActionState.name_event.set()

    else:
        await message.message.answer(
            "Напишите комментарий (чтобы пропустить поставьте 0)"
        )
        await UserActionState.comment.set()


@dp.message_handler(state=UserActionState.comment)
async def take_part_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция take_part_2. Запускается по изменению состояния.
    Проверяет введённый текс. Если 0, то выводит список событий.
    Иначе, записывает текст в БД и выводит список событий.
    """
    input_text = message.text.capitalize()
    async with state.proxy() as data:
        id_user = data["id_telegram"]
        event = data["event"]

    if input_text != "0":
        await message.answer("Вы приняли участие. Комментарий записан.")
        database.add_participation(
            id_user=id_user, id_event=event[0][0], comment=input_text
        )
        await state.finish()

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.answer("Выберите событие:", reply_markup=kb)
            await UserActionState.name_event.set()
        else:
            await message.answer("События ещё не добавлены.")

    else:
        await message.answer("Вы приняли участие.")
        database.add_participation(id_user=id_user, id_event=event[0][0])
        await state.finish()

        list_events = database.gets_events()
        if list_events:
            kb = list_button(list_events)
            await message.answer("Выберите событие:", reply_markup=kb)
            await UserActionState.name_event.set()
        else:
            await message.answer("События ещё не добавлены.")
