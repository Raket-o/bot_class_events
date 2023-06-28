"""Модуль хранения данных (состояний) пользователя"""
from aiogram.dispatcher.filters.state import StatesGroup, State


class UserInfoState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    user_id = State()
    user_name = State()
    country = State()
    city = State()
    city_area = State()
    id_city_area = State()
    list_city_area = State()
    qty_hotels = State()
    id_hotels = State()
    list_id_hotels = State()
    # need_photo = State()
    # qty_photo = State()
    phone_number = State()
    data_check_in = State()
    data_check_out = State()
    command = State()
    method_sort = State()


class Hotels(StatesGroup):
    """ Класс Hotels. Хранит данные отелей"""
    hotels_id = State()
    hotels_name = State()
    hotels_price = State()
