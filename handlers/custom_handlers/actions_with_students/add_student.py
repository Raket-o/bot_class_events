""" Модуль обработки каллбэка с датой operations_events"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp
from states.states import AddUserState


@dp.callback_query_handler(lambda callback_query: callback_query.data == "add_students")
async def add_student_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функция add_student_1. Каллбэка с датой add_students запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer(
        "Введите фамилию и имя ученика\n (пример- Иванов Иван):"
    )
    await AddUserState.student_name.set()


@dp.message_handler(state=AddUserState.student_name)
async def add_student_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция add_student_2. Добавляет нового ученика с уникальным паролем.
    """
    password = database.add_student(message.text.title())
    kb = admin_bts_stud()
    await message.answer(
        f"Пользователь добавлен.\n Пароль для входа: {password}", reply_markup=kb
    )
    await state.finish()
