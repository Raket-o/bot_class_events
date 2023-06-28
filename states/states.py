"""Модуль хранения данных (состояний) пользователя"""
from aiogram.dispatcher.filters.state import StatesGroup, State


class UserInfoState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    telegram_id = State()
    user_first_name = State()
    user_last_name = State()
    student_name = State()


class AdminInfoState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    change_eve_st = State()
    user_first_name = State()
    user_last_name = State()
    student_name = State()


class AddUserState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    student_name = State()

