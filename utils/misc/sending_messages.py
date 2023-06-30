from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from loader import bot
from database import database
from states.states import SendingMessageState
from keyboards.inline.admin_buttons import admin_bts


async def sending_messages(text_message):
    all_student = database.gets_students()
    for i in all_student:
        if i[1] != 0:
            await bot.send_message(chat_id=i[1], text=text_message, parse_mode="HTML")


@dp.callback_query_handler(lambda callback_query: callback_query.data == "all_sending_message")
async def add_event_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    await message.message.answer('Введите тест:')
    await SendingMessageState.message_text.set()


@dp.message_handler(state=SendingMessageState.message_text)
async def add_event_2(message: types.Message, state: FSMContext) -> None:
    input_text = message.text.capitalize()
    await sending_messages(input_text)

    kb = admin_bts()
    await message.answer('Сообщения отправлены', reply_markup=kb)
    await state.finish()