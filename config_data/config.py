"""Модуль конфиг для проверки создано ли окружение."""
import os


from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_LOG = os.getenv("ADMIN_LOG").title()
ADMIN_PASS = os.getenv("ADMIN_PASS")

DEFAULT_COMMANDS = (
    ('start', "Запустить бота")
)
