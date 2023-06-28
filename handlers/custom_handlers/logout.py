import logging
from aiogram import types
from loader import dp
from states.states import UserInfoState, AdminInfoState
from aiogram.dispatcher import FSMContext
from database import database

from keyboards import reply
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from keyboards.reply.list_button import list_button


@dp.message_handler(text="Ученики")
async def students(message: types.Message, state: FSMContext) -> None:
    kb = admin_bts_stud()
    await message.answer('Текущие события:', reply_markup=kb)


