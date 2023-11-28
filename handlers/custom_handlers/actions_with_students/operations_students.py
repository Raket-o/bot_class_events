""" Модуль обработки каллбэка с датой operations_students"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp


@dp.callback_query_handler(lambda callback_query: callback_query.data == "operations_students")
async def operations_students(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функция operations_students. Каллбэка с датой operations_students запускает данную функцию.
    Выводит клавиатуру с действиями по событиям и завершает ожидания состояния.
    """
    kb = admin_bts_stud()
    await message.message.answer("Выберите действие:", reply_markup=kb)
    await state.finish()


