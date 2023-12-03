""" Модуль обработки каллбэка с датой edit_pass_students"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp
from states.states import ResPassUserState


@dp.callback_query_handler(
    lambda callback_query: callback_query.data == "edit_pass_students"
)
async def edit_student_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функция edit_student_1. Каллбэка с датой edit_pass_students запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer("Введите ИД:")
    await ResPassUserState.id.set()


@dp.message_handler(state=ResPassUserState.id)
async def edit_student_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция del_student_2. Проверяет на валидность введённый ИД ученика и изменяет пароль.
    """
    try:
        id = int(message.text)
        data_user = database.check_users_by_id(id)
        if data_user:
            new_password = database.reset_password_users_by_id(id)
            kb = admin_bts_stud()
            await message.answer(f"Новый пароль: {new_password}", reply_markup=kb)
            await state.finish()
        else:
            await message.answer("Такой ИД я не нахожу. Попробуйте ещё раз.")
    except ValueError:
        await message.answer("ИД может содержать только фиры. Попробуйте ещё раз.")
