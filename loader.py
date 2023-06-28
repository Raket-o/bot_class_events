from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_data import config

async def start_up(_):
    print("Bot started")

async def on_shutdown(_):
    print("Bot stopped")

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

