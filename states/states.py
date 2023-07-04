"""Модуль хранения данных (состояний) пользователя"""

from aiogram.dispatcher.filters.state import StatesGroup, State


class UserInfoState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    telegram_id = State()
    user_first_name = State()
    user_last_name = State()
    student_name = State()
    password = State()
    comment = State()


class AdminInfoState(StatesGroup):
    """ Класс AdminInfoState. Хранит информацию и данные вводимые пользователем"""
    change_eve_st = State()
    user_first_name = State()
    user_last_name = State()
    student_name = State()


class AddUserState(StatesGroup):
    """ Класс AddUserState. Хранит информацию и данные вводимые пользователем"""
    student_name = State()


class EditUserState(StatesGroup):
    """ Класс EditUserState. Хранит информацию и данные вводимые пользователем"""
    id = State()
    student_name = State()


class ResPassUserState(StatesGroup):
    """ Класс ResPassUserState. Хранит информацию и данные вводимые пользователем"""
    id = State()


class DelUserState(StatesGroup):
    """ Класс DelUserState. Хранит информацию и данные вводимые пользователем"""
    id = State()


class BlockUserState(StatesGroup):
    """ Класс UserInfoState. Хранит информацию и данные вводимые пользователем"""
    id = State()


class EventState(StatesGroup):
    """ Класс EventState. Хранит информацию и данные вводимые пользователем"""
    name = State()
    deadline = State()
    description = State()


class EventEditState(StatesGroup):
    """ Класс EventEditState. Хранит информацию и данные вводимые пользователем"""
    id = State()
    name = State()
    deadline = State()
    description = State()


class EventDelState(StatesGroup):
    """ Класс EventDelState. Хранит информацию и данные вводимые пользователем"""
    id = State()


class SendingMessageState(StatesGroup):
    """ Класс SendingMessageState. Хранит информацию и данные вводимые пользователем"""
    message_text = State()


class UserActionState(StatesGroup):
    """ Класс UserActionState. Хранит информацию и данные вводимые пользователем"""
    name_student = State()
    event = State()
    name_event = State()
    comment = State()


class GetDetailEventState(StatesGroup):
    """ Класс GetDetailEventState. Хранит информацию и данные вводимые пользователем"""
    id_event = State()








