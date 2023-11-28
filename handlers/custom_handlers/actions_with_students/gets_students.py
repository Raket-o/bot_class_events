""" Модуль обработки каллбэка с датой get_students"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp


@dp.callback_query_handler(lambda callback_query: callback_query.data == "get_students", state="*")
async def gets_student(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функия gets_student. Каллбэка с датой get_students запускает данную функцию.
    Выводит информацию по всем ученикам.
    """
    res = database.gets_students()
    await message.message.answer('Список учеников:\n')
    for i in res:
        if i[6]:
            status = "Заблокирован"
        else:
            status = "Разблокирован"

        await message.message.answer(
            f"Ид: {i[0]}\n ФИ: {i[4]}\n Пароль: {i[5]}\n Статус: {status}\n Последний вход: {i[7]}"
        )

    kb = admin_bts_stud()
    await message.message.answer('Админ меню:', reply_markup=kb)
    await state.finish()
