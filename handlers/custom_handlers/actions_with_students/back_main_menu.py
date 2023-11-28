""" Модуль обработки каллбэка с датой main_menu"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.admin_buttons import admin_bts
from loader import dp


@dp.callback_query_handler(lambda callback_query: callback_query.data == "main_menu")
async def main_menu(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функция main_menu. Каллбэка с датой main_menu запускает данную функцию.
    Завершает ожидание состояния и клавиатуру "Админ меню"
    """
    kb = admin_bts()
    await message.message.answer("Админ меню:", parse_mode="HTML", reply_markup=kb)
    await state.finish()
