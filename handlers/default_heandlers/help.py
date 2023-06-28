from aiogram import types
from loader import dp
from keyboards.inline import back_main_menu


__HELP_MESSAGE = """<b>/low</b> - <em>самая низкая стоимость,
самые доступные авто, самое близкое местоположение и так далее.</em>
<b>/high</b> - <em>самая высокая стоимость,
самые дорогие авто, самое удалённое местоположение и так далее.</em>
<b>/custom</b> - <em>фильтр поиска цена от и до, расстояние от и до, срок от и до и так далее.</em>
<b>/history</b> -  <em>краткая история запросов пользователя.</em>
"""


@dp.message_handler(commands=["help"])
async def stars_command(message: types.Message):
    await message.answer(__HELP_MESSAGE, parse_mode="HTML", reply_markup=main_menu.callback_main_menu())


