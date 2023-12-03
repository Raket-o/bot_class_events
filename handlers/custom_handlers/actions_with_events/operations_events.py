""" Модуль обработки каллбэка с датой operations_events"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.admin_bts_oper_events import admin_bts_eve
from loader import dp


@dp.callback_query_handler(
    lambda callback_query: callback_query.data == "operations_events"
)
async def operations_events(
    message: [types.CallbackQuery, types.Message], state: FSMContext
) -> None:
    """
    Функция operations_events. Каллбэка с датой operations_events запускает данную функцию.
    Выводит клавиатуру с действиями по событиям и завершает ожидания состояния.
    """
    kb = admin_bts_eve()
    await message.message.answer("Выберите действие:", reply_markup=kb)
    await state.finish()
