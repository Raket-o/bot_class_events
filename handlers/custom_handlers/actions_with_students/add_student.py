from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start
from states.states import AddUserState

from keyboards.reply.list_button import list_button
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from database import database


@dp.callback_query_handler(lambda callback_query: callback_query.data == "add_students")
async def operations_students(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите фамилию и имя ученика\n (пример- Иванов Иван):')
    await AddUserState.student_name.set()


@dp.message_handler(state=AddUserState.student_name)
async def get_name_student(message: types.Message, state: FSMContext) -> None:
    password = database.add_student(message.text.title())
    kb = admin_bts_stud()
    await message.answer(f'Пользователь добавлен.\n Пароль для входа: {password}', reply_markup=kb)
    await state.finish()

