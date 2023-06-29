from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import DelUserState
from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


@dp.callback_query_handler(lambda callback_query: callback_query.data == "delete_students")
async def del_student(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите ИД:')
    await DelUserState.id.set()


@dp.message_handler(state=DelUserState.id)
async def del_student_2(message: types.Message, state: FSMContext) -> None:
    try:
        id = int(message.text)
        data_user = database.check_users_by_id(id)
        if data_user:
            database.del_users_by_id(id)
            kb = admin_bts_stud()
            await message.answer('Ученик удалён.', reply_markup=kb)
            await state.finish()
        else:
            await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    except ValueError:
        await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')
