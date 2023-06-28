# from loader import bot
# import handlers
# from telebot import custom_filters
# from telebot.custom_filters import StateFilter
# from utils.set_bot_commands import set_default_commands
from aiogram import executor
from loader import dp, start_up, on_shutdown
from handlers.default_heandlers import start
from utils.logging import logger_root
from database import database
import logging

if __name__ == '__main__':
    logger = logging.getLogger("logger_main")

    database.init_db()
    logger.info("Bot starting")

    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=start_up,
                           on_shutdown=on_shutdown)
    logger.info("Bot STOP")


    # bot.add_custom_filter(custom_filter=StateFilter(bot))
    # set_default_commands(bot)
    # bot.polling(none_stop=True, interval=0)
