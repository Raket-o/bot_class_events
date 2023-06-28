from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from handlers.default_heandlers import start

from keyboards.reply.list_button import list_button
from keyboards.inline.admin_bts_oper_stud import admin_bts_stud
from keyboards.inline.admin_bts_oper_events import admin_bts_eve

from states.states import AdminInfoState


@dp.message_handler(state=AdminInfoState.change_eve_st)
async def get_met_sort_low(message: types.Message, state: FSMContext) -> None:
    input_text_user = message.text.title()

    if input_text_user == "Ученики":
        print("Ученики")
        kb = admin_bts_stud()
        await message.answer('Выберите действие.', reply_markup=kb)

    elif input_text_user == "События":
        print("События")
        kb = admin_bts_eve()
        await message.answer('Выберите действие.', reply_markup=kb)

    else:
        await message.answer('Непонятное действие, выберите из предложенных.')




# @dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('operations_events'))
# @dp.callback_query_handler(lambda c: c.data == 'operations_students')
# @dp.callback_query_handler(lambda callback_query: callback_query.data == "operations_events")
# async def operations_students(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
# # async def oper_stud(message: types.Message) -> None:
#
#     """
#     Функия main_menu. Каллбэка с датой main_menu запускает данную функцию.
#     Завершает ожидание состояния и выводит текст (главного меню)
#     """
#     # lst_buttons = ["Просмотреть", "Создать", "Редактировать", "Удалить", "Вернуться"]
#     # kb = list_button(lst_buttons)
#     # await state.finish()
#
#     kb = admin_bts()
#     # print(kb)
#     # await message.reply("Выберите действие:", reply_markup=kb)
#     await message.answer("Выберите действие:", reply_markup=kb)
#     # await message.reply("Выберите действие:")
#
#
#
#     # await message.message("Выберите действие:")