""" Модуль обработки каллбэка с датой main_menu"""
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from database import database
from keyboards.reply import list_button
from keyboards.inline import admin_buttons


@dp.callback_query_handler(lambda callback_query: callback_query.data == "get_students", state="*")
async def main_menu(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:

    """
    Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
    Завершает ожидание состояния и выводит текст (главного меню)
    """

    # await message.message.delete()

    res = database.gets_students()
    await message.message.answer('Список учеников:\n')
    for i in res:
        if i[6]:
            status = "Заблокирован"
        else:
            status = "Разблокирован"

        await message.message.answer(
            f"Ид: {i[0]}\n ФИ: {i[4]}\n Пароль: {i[5]}\n Статус: {status}"
        )

    kb = admin_bts_stud()
    await message.message.answer('Админ меню:', reply_markup=kb)
    await state.finish()
