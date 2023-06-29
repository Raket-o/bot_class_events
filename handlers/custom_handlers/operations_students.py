from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start

from keyboards.reply.list_button import list_button
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


@dp.callback_query_handler(lambda callback_query: callback_query.data == "operations_students")
async def operations_students(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
#     """
#     Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
#     Завершает ожидание состояния и выводит текст (главного меню)
#     """
    kb = admin_bts_stud()
    await message.message.answer("Выберите действие:", reply_markup=kb)
    await state.finish()


