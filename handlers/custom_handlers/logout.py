""" Модуль обработки каллбэка с датой logout"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.default_heandlers import start
from loader import dp
from states.states import UserInfoState


@dp.callback_query_handler(lambda callback_query: callback_query.data == "logout")
async def logout(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    """
    Функия logout. Каллбэка с датой logout запускает данную функцию.
    Разлогинивается
    """
    await state.finish()
    await message.message.answer(start.START_MESSAGE, parse_mode="HTML")
    await UserInfoState.student_name.set()

