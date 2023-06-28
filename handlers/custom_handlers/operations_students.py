from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start

from keyboards.reply.list_button import list_button
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud


@dp.callback_query_handler(lambda callback_query: callback_query.data == "operations_students")
async def operations_students(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
# # async def oper_stud(message: types.Message) -> None:
#
#     """
#     Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
#     Завершает ожидание состояния и выводит текст (главного меню)
#     """
#     # lst_buttons = ["Просмотреть", "Создать", "Редактировать", "Удалить", "Вернуться"]
#     # kb = list_button(lst_buttons)
#     # await state.finish()

    # await message.message.delete()
    kb = admin_bts_stud()
    # print(kb)
    # await message.reply("Выберите действие:", reply_markup=kb)
    await message.message.answer("Выберите действие:", reply_markup=kb)
    # await message.reply("Выберите действие:")
#
#
#
#     # await message.message("Выберите действие:")



