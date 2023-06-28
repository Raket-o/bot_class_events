""" Модуль обработки каллбэка с датой main_menu"""
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start
from keyboards.inline.admin_buttons import admin_bts


@dp.callback_query_handler(lambda callback_query: callback_query.data == "main_menu", state="*")
async def main_menu(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
    Завершает ожидание состояния и выводит текст (главного меню)
    """
    await state.finish()
    kb = admin_bts()
    await message.message.answer(start.START_MESSAGE, parse_mode="HTML", reply_markup = kb)

    # await message.message.answer(start.START_MESSAGE, parse_mode="HTML")
    # await start.stars_command()

