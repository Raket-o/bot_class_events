from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import UserActionState, UserInfoState
from database import database
from keyboards.inline.admin_bts_oper_events import admin_bts_eve
import datetime
from handlers.custom_handlers.home_page import input_password

from keyboards.reply.list_button import list_button



@dp.callback_query_handler(lambda callback_query: callback_query.data == "take_part")
async def take_part_1(message: [types.CallbackQuery, types.Message], state: FSMContext) -> None:
    async with state.proxy() as data:
        id_telegram = data["id_telegram"]
        event = data["event"]
        # print(data)

    participation = database.check_participation(id_user=id_telegram, id_event=event[0][0])
    if participation:
        # database.del_participation(id_student=id_telegram, id_event=event[0][0])

        await message.message.answer('Вы уже приняли участие.')

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
            # await state.finish()
    else:

        # *******************************************
        # list_events = database.gets_events()
        # # print(list_events)
        # if list_events:
        #     # await state.finish()
        #
        #     kb = list_button(list_events)
        #     await message.message.answer('Выберите событие:', reply_markup=kb)
        #     # await state.finish()
        #     await UserActionState.name_event.set()

        await message.message.answer('Напишите комментарий (чтобы пропустить поставьте 0)')
        await UserActionState.comment.set()




    # await state.finish()

    # при нажатии подписать-отписать
        # делаем делаем запрос- получаем ИД-ивента
        # смотрим подписан уже нет
            # если нет, то запрашиваем коммент, записываем в новую таблицу
        # если подписан, то удалфем из новой таблицы запись

    # await message.message.answer('Введите ИД:')

    # id_event = database.get_event_by_name(message.message.text)
    # print(id_event)

    # await UserActionState.name_event.set()


@dp.message_handler(state=UserActionState.comment)
async def take_part_2(message: types.Message, state: FSMContext) -> None:
    input_text = message.text
    async with state.proxy() as data:
        id_user = data["id_telegram"]
        event = data["event"]
        # print("refuse_participate_event_2", data)


    # await state.finish()
    if input_text != "0":
        await message.answer('Вы приняли участие. Комментарий записан.')
        database.add_participation(id_user=id_user, id_event=event[0][0], comment=input_text)

        await state.finish()

        # *******************************************
        list_events = database.gets_events()
        # print(list_events)
        if list_events:
            # await state.finish()

            kb = list_button(list_events)
            await message.answer('Выберите событие:', reply_markup=kb)
            # await state.finish()
            await UserActionState.name_event.set()
            # await state.finish()


        else:
            await message.answer('События ещё не добавлены.')  # разлогиниться добавить кнопку выход


    else:
        await message.answer('Вы приняли участие.')
        database.add_participation(id_user=id_user, id_event=event[0][0])

        await state.finish()


        # *******************************************
        list_events = database.gets_events()
        # print(list_events)
        if list_events:
            # await state.finish()

            kb = list_button(list_events)
            await message.answer('Выберите событие:', reply_markup=kb)
            # await state.finish()
            await UserActionState.name_event.set()
            # await state.finish()


        else:
            await message.answer('События ещё не добавлены.')  # разлогиниться добавить кнопку выход



    #     id = int(message.text)
    #     data_event = database.check_event_by_id(id)
    #     # print(data_event)
    #     if data_event:
    #         await message.answer('Новое название или введите цифру 0, чтоб его не изменять.')
    #
    #         async with state.proxy() as data:
    #             data["id"] = id
    #             data["name"] = data_event[3]
    #             data["deadline"] = data_event[4]
    #             data["description"] = data_event[5]
    #
    #
    #         await EventEditState.name.set()
    #
    #     else:
    #         await message.answer('Такой ИД я не нахожу. Попробуйте ещё раз.')
    # except ValueError:
    #     await message.answer('ИД может содержать только фиры. Попробуйте ещё раз.')


# @dp.message_handler(state=UserActionState.name)
# async def edit_events_3(message: types.Message, state: FSMContext) -> None:
#     input_text = message.text.capitalize()
#
#     await message.answer('Новая дата (пример- 01.01.2023) или\n введите цифру 0, чтоб его не изменять.')
#
#     if input_text != "0":
#         async with state.proxy() as data:
#             data["name"] = input_text
#         await EventEditState.deadline.set()
#     else:
#         await EventEditState.deadline.set()
#
#
# @dp.message_handler(state=EventEditState.deadline)
# async def edit_events_4(message: types.Message, state: FSMContext) -> None:
#     input_text = message.text
#     if input_text != "0":
#         try:
#             input_date = datetime.datetime.strptime(message.text, "%d.%m.%Y").date()
#
#             async with state.proxy() as data:
#                 data["deadline"] = input_date
#             await EventEditState.description.set()
#
#             await message.answer('Полное описание с ценами и прочим:')
#         except ValueError:
#             await message.answer('Введена некорректная дата. НЕ ИЗМЕНЕНО!')
#
#     else:
#         await message.answer('Новое описание или или введите цифру 0, чтоб его не изменять')
#         await EventEditState.description.set()
#
#
# @dp.message_handler(state=EventEditState.description)
# async def edit_events_5(message: types.Message, state: FSMContext) -> None:
#     input_text = message.text
#
#     if input_text != "0":
#         async with state.proxy() as data:
#             data["description"] = input_text
#             database.edit_event_by_id(
#                 data["id"],
#                 data["name"],
#                 data["deadline"],
#                 data["description"]
#             )
#
#         kb = admin_bts_eve()
#         await message.answer('Изменения внесены.', reply_markup=kb)
#         await state.finish()
#
#     else:
#         async with state.proxy() as data:
#             database.edit_event_by_id(
#                 data["id"],
#                 data["name"],
#                 data["deadline"],
#                 data["description"]
#             )
#         kb = admin_bts_eve()
#         await message.answer('Изменения внесены.', reply_markup=kb)
#         await state.finish()
