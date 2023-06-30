from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import UserActionState, UserInfoState
from database import database
from keyboards.inline.admin_bts_oper_events import admin_bts_eve
import datetime
from handlers.custom_handlers.home_page import input_password

from keyboards.reply.list_button import list_button



@dp.callback_query_handler(lambda callback_query: callback_query.data == "back_to_list_event")
async def take_part_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
        await state.finish()
        # *******************************************
        list_events = database.gets_events()
        # print(list_events)
        if list_events:
            # await state.finish()

            kb = list_button(list_events)
            await message.message.answer('Выберите событие:', reply_markup=kb)
            # await state.finish()
            await UserActionState.name_event.set()

