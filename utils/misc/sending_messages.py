""" Модуль массовой рассылки сообщения"""

from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from loader import bot
from database import database
from states.states import SendingMessageState
from keyboards.inline.admin_buttons import admin_bts


@dp.callback_query_handler(lambda callback_query: callback_query.data == "all_sending_message")
async def custom_sending_messages_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функия custom_sending_messages_1.
    Каллбэка с датой all_sending_message запускает данную функцию.
    Ожидает состояние.
    """
    await message.message.answer('Введите тест:')
    await SendingMessageState.message_text.set()


@dp.message_handler(state=SendingMessageState.message_text)
async def custom_sending_messages_2(message: types.Message, state: FSMContext) -> None:
    """
    Функия custom_sending_messages_2. Передаёт текст в функцию массовой рассылки.
    """
    input_text = message.text.capitalize()
    await sending_messages(input_text)

    kb = admin_bts()
    await message.answer('Сообщения отправлены', reply_markup=kb)
    await state.finish()


async def sending_messages(text_message: str) -> None:
    """
    Функция sending_messages. Запрашивает всех пользователей. И у кого есть
    ИД телеграмм, отправляет им сообщения.
    :param text_message: Текст сообщения
    """
    all_users = database.gets_students()
    for i in all_users:
        if i[1] != 0:
            await bot.send_message(chat_id=i[1], text=text_message, parse_mode="HTML")
