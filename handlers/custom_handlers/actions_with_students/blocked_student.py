""" Модуль обработки каллбэка с датой main_menu"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from loader import dp
from states.states import BlockUserState


@dp.callback_query_handler(lambda callback_query: callback_query.data == "blocked_students")
async def blocked_student_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функция blocked_student_1. Каллбэка с датой blocked_students запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer('Введите ИД:')
    await BlockUserState.id.set()


@dp.message_handler(state=BlockUserState.id)
async def blocked_student_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция blocked_student_2. Проверяет на валидность введённый ИД ученика и
    блокирует вход.
    """
    try:
        id = int(message.text)
        data_user = database.check_users_by_id(id)
        print(data_user)
        if data_user:
            if data_user[6] == 0:
                database.blocked_users_by_id(data_user[0], True)
                kb = admin_bts_stud()
                await message.answer('Ученик заблокирован.', reply_markup=kb)
                await state.finish()
            else:
                database.blocked_users_by_id(data_user[0], False)
                kb = admin_bts_stud()
                await message.answer('Ученик разблокирован.', reply_markup=kb)
                await state.finish()

        else:
            await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    except ValueError:
        await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')
