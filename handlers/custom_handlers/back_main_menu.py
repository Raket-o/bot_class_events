""" Модуль обработки каллбэка с датой main_menu"""
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start


@dp.callback_query_handler(lambda callback_query: callback_query.data == "main_menu", state="*")
async def main_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
    Завершает ожидание состояния и выводит текст (главное меню)
    """
    await state.finish()
    await callback.message.answer(start.START_MESSAGE, parse_mode="HTML")