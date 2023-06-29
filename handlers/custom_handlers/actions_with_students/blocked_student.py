from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import BlockUserState
from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


@dp.callback_query_handler(lambda callback_query: callback_query.data == "blocked_students")
async def blocked_student(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    print()
    await message.message.answer('Введите ИД:')
    await BlockUserState.id.set()


@dp.message_handler(state=BlockUserState.id)
async def blocked_student_2(message: types.Message, state: FSMContext) -> None:
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
