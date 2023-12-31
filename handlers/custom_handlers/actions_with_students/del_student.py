""" Модуль обработки каллбэка с датой delete_students"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp
from states.states import DelUserState


@dp.callback_query_handler(
    lambda callback_query: callback_query.data == "delete_students"
)
async def del_student(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функция del_student. Каллбэка с датой delete_students запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer("Введите ИД:")
    await DelUserState.id.set()


@dp.message_handler(state=DelUserState.id)
async def del_student_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция del_student_2. Проверяет на валидность введённый ИД ученика и
    удаляет из БД.
    """
    try:
        id = int(message.text)
        data_user = database.check_users_by_id(id)
        if data_user:
            database.del_users_by_id(id)
            kb = admin_bts_stud()
            await message.answer("Ученик удалён.", reply_markup=kb)
            await state.finish()
        else:
            await message.answer("Такой ИД я не нахожу. Попробуйте ещё раз.")
    except ValueError:
        await message.answer("ИД может содержать только фиры. Попробуйте ещё раз.")
