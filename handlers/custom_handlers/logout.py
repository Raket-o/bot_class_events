import logging
from aiogram import types
from loader import dp
from states.states import UserInfoState, AdminInfoState
from aiogram.dispatcher import FSMContext
from database import database

from keyboards import reply
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from keyboards.reply.list_button import list_button
from handlers.default_heandlers import start


@dp.callback_query_handler(lambda callback_query: callback_query.data == "logout")
async def logout(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
#     """
#     Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
#     Завершает ожидание состояния и выводит текст (главного меню)
#     """

    await state.finish()
    await message.message.answer(start.START_MESSAGE, parse_mode="HTML")
    await UserInfoState.student_name.set()

