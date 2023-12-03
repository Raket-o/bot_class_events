""" Модуль обработки каллбэка с датой get_events_detal"""

from aiogram import types
from aiogram.dispatcher import FSMContext

from database import database
from keyboards.inline.admin_bts_oper_events import admin_bts_eve
from loader import dp
from states.states import GetDetailEventState


@dp.callback_query_handler(
    lambda callback_query: callback_query.data == "get_events_detal"
)
async def get_events_detal_1(message: [types.CallbackQuery, types.Message]) -> None:
    """
    Функция get_events_detal_1.
    Ожидает состояние.
    """
    await message.message.answer("Введите ИД:")
    await GetDetailEventState.id_event.set()


@dp.message_handler(state=GetDetailEventState.id_event)
async def get_events_detal_2(message: types.Message, state: FSMContext) -> None:
    """
    Функция get_events_detal_2. Проверяет введённого валидность ИД события.
    И выводит детальную информацию по событию.
    """
    try:
        id_event = int(message.text)
        data_event = database.check_event_by_id(id_event)

        if data_event:
            event = database.get_detail_event(id_event)

            try:
                await message.answer(
                    f"Название: {event[0][0]}\n Дата завершения: {event[0][1]}\n Описание: {event[0][2]}"
                )
                for i in event:
                    comment = i[4]
                    if i[4] == "None":
                        comment = "Без комментарий"

                    await message.answer(
                        f"Участник: {i[3]}\n     Комментарий: {comment}\n"
                    )

            except IndexError:
                pass

            finally:
                kb = admin_bts_eve()
                await message.answer("Выберите действие:", reply_markup=kb)
                await state.finish()

        else:
            await message.answer("Такой ИД я не нахожу. Попробуйте ещё раз.")
    except ValueError:
        await message.answer("ИД может содержать только фиры. Попробуйте ещё раз.")
