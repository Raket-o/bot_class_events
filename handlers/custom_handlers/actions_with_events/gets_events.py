""" Модуль обработки каллбэка с датой main_menu"""
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from database import database
from keyboards.reply import list_button
from keyboards.inline.admin_bts_oper_events import admin_bts_eve


@dp.callback_query_handler(lambda callback_query: callback_query.data == "get_events", state="*")
async def get_events(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:

    """
    Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
    Завершает ожидание состояния и выводит текст (главного меню)
    """

    res = database.gets_events()

    await message.message.answer('Список событий:\n')
    for i in res:
        qty_part = database.qty_part_event(i[0])
        await message.message.answer(
            f"Ид: {i[0]}\n Название: {i[3]}\n Дата завершения: {i[4]}\n"
            f" Описание: {i[5]}\n Количество участников: {qty_part[0][0]} "
        )

    kb = admin_bts_eve()
    await message.message.answer('Админ меню:', reply_markup=kb)
    await state.finish()