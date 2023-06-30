from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import EditUserState
from database import database
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


@dp.callback_query_handler(lambda callback_query: callback_query.data == "edit_students")
async def edit_student(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите ИД:')
    await EditUserState.id.set()


@dp.message_handler(state=EditUserState.id)
async def edit_student_2(message: types.Message, state: FSMContext) -> None:
    try:
        id = int(message.text)
        data_user = database.check_users_by_id(id)
        if data_user:

            await message.answer('Введите фамилию и имя ученика.')

            async with state.proxy() as data:
                data["id"] = id

            await EditUserState.student_name.set()

        else:
            await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    except ValueError:
        await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')


@dp.message_handler(state=EditUserState.student_name)
async def edit_student_3(message: types.Message, state: FSMContext) -> None:
    input_text_user = message.text.title()

    async with state.proxy() as data:
        id = data["id"]
    database.edit_users_by_id(id, input_text_user)

    kb = admin_bts_stud()
    await message.answer('Изменения внесены.', reply_markup=kb)
    await state.finish()




