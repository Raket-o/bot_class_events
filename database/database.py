""" Модуль работы с базой данных"""

import sqlite3
import random
import datetime
from typing import List, Any


def init_db() -> None:
    """ Функция init_db. При отсутствии базы донной создаёт ёё. """
    with sqlite3.connect('database/database.db') as conn:

        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            PRAGMA foreign_keys = ON
            """
        )
        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_events';
            """
        )
        tab_event = cursor.fetchone()

        cursor.execute(
            """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='table_users';
            """
        )
        tab_users = cursor.fetchone()

    cursor.execute(
        """
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='table_part_and_comm';
        """
    )
    tab_part_and_comm = cursor.fetchone()

    # exists: Optional[tuple[str, ]] = cursor.fetchone()
    # now in `exist` we have tuple with table name if table really exists in DB

    if not tab_event:
        cursor.executescript(
            """
            CREATE TABLE `table_events` (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author_id INTEGER DEFAULT 0,
                author_name TEXT DEFAULT NULL,
                name_event TEXT DEFAULT NULL,
                deadline DATE,
                description TEXT DEFAULT NULL,
            )
            """
        )

    if not tab_users:
        cursor.executescript(
            """
            CREATE TABLE `table_users` (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER DEFAULT 0,
                user_first_name TEXT DEFAULT NULL,
                user_last_name TEXT DEFAULT NULL,
                student_name TEXT DEFAULT NULL,
                password TEXT DEFAULT NULL,
                blocked BOOL DEFAULT False,
                last_login DATE
            )
            """
        )

        cursor.execute(
            """
            INSERT INTO table_users (student_name, password) VALUES ("1", "1")
            """
        )

    if not tab_part_and_comm:
        cursor.executescript(
            """
            CREATE TABLE `table_part_and_comm` (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_telegram INTEGER,
                id_event INTEGER,                
                comment TEXT DEFAULT NULL,
                FOREIGN KEY (id_telegram) references table_users(telegram_id) ON DELETE CASCADE,
                FOREIGN KEY (id_event) references table_events(id) ON DELETE CASCADE
            )
            """
        )
    conn.commit()


def check_users(name: str) -> list[Any]:
    """
    Функция check_users. Проверяет есть ли введённое имя (при логине).
    :param name: Введённое имя (при логине)
    :return: Результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id
            FROM table_users
            WHERE student_name == ?
            """,
            (name, )
        )
        check_user = cursor.fetchall()
        return check_user


def check_password(student_name: str, password: str) -> list[Any]:
    """
    Функцию check_password. Проверяет введённый пароль (при логине).
    :param student_name: Имя школьника
    :param password: Введённый пароль (при логине)
    :return: Результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id
            FROM table_users
            WHERE student_name == ? AND password == ? AND blocked == False
            """,
            (student_name, password, )
        )
        check_pass = cursor.fetchone()
        return check_pass


def update_info_for_db(telegram_id: int,
                       user_first_name: str,
                       user_last_name: str,
                       student_name: str) -> None:
    """
    Функция update_info_for_db. При логине, обновляет данные.
    :param telegram_id: ИД телеграмма
    :param user_first_name: Имя пользователя
    :param user_last_name: Фамилию пользователя
    :param student_name: Имя школьника
    """
    cur_datetime = datetime.datetime.now().replace(microsecond=0)

    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET telegram_id = ?, user_first_name = ?, user_last_name = ?, last_login = ?
            WHERE student_name = ?;
            """,
            (telegram_id, user_first_name, user_last_name, cur_datetime, student_name)
        )
        conn.commit()


def gets_events() -> list[Any]:
    """
    Функция gets_events. Находит все события и возвращает их.
    :return: Список событий
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_events
            """
        )
        list_events = cursor.fetchall()
        return list_events


def gets_students() -> list[Any]:
    """
    Функция gets_events. Находит всех школьников и возвращает их.
    :return: Список пользователей
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_users
            """
        )
        list_users = cursor.fetchall()
        return list_users


def add_student(name_student: str) -> str:
    """
    Функция add_student. Добавляет нового школьника.
    :param name_student: Имя школьника
    :return: сгенерированный пароль
    """
    password = create_password()
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO table_users (student_name, password) VALUES (?, ?);
            """,
            (name_student, password, )
        )
        conn.commit()
        return password


def check_users_by_id(id: int) -> list[Any]:
    """
    Функция check_users_by_id. Находит пользователя по ИД.
    :param id: ИД пользователя
    :return: результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_users
            WHERE id == ?
            """,
            (id, )
        )
        user = cursor.fetchone()
        return user


def edit_users_by_id(id: int, name: str) -> None:
    """
    Функция edit_users_by_id. Обновляет данные о школьнике.
    :param id: ИД пользователя
    :param name: Имя школьника
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET student_name = ?
            WHERE id = ?;
            """,
            (name, id)
        )
        conn.commit()


def reset_password_users_by_id(id: int) -> str:
    """
    Функция reset_password_users_by_id. Генерирует новый пароль.
    :param id: ИД пользователя
    :return: новый сгенерированный пароль
    """
    password = create_password()
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET password = ?
            WHERE id = ?;
            """,
            (password, id)
        )
        conn.commit()
        return password


def del_users_by_id(id: int) -> None:
    """
    Функция del_users_by_id. Удаляет пользователя.
    :param id: ИД пользователя
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM table_users 
            WHERE id == ?            
            """,
            (id, )
        )
        conn.commit()


def blocked_users_by_id(id: int, status: bool) -> None:
    """
    Функция blocked_users_by_id. Блокирует\разблокирует пользователя по ИД.
    :param id: ИД пользователя
    :param status: Статус пользователя
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET blocked = ?
            WHERE id = ?;
            """,
            (status, id)
        )
        conn.commit()


def add_event_db(author_id: int,
                 author_name: str,
                 name_event:str,
                 deadline: datetime,
                 description: str) -> None:
    """
    Функция add_event_db. Добавляет новое событие.
    :param author_id: ИД автора
    :param author_name: Имя автора
    :param name_event: Название события
    :param deadline: Крайний срок события
    :param description: Описание
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO table_events (author_id, author_name, name_event, deadline, description) VALUES (?, ?, ?, ?, ?);
            """,
            (author_id, author_name, name_event, deadline, description, )
        )
        conn.commit()


def check_event_by_id(id: int) -> list[Any]:
    """
    Функция check_event_by_id. Существует ли событие по ИД.
    :param id: ИД события
    :return: результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_events
            WHERE id == ?
            """,
            (id, )
        )
        event = cursor.fetchone()
        return event


def edit_event_by_id(id: int,
                     name: str,
                     deadline: datetime,
                     description: str) -> None:
    """
    Функция edit_event_by_id. Изменяет данные о событии.
    :param id: ИД события
    :param name: Название события
    :param deadline: Крайний срок события
    :param description: Описание
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_events
            SET name_event = ?, deadline = ?, description = ? 
            WHERE id = ?;
            """,
            (name, deadline, description, id, )
        )
        conn.commit()


def del_event_by_id(id: int) -> None:
    """
    Функция del_event_by_id. Удаляет событие.
    :param id: ИД события
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM table_events 
            WHERE id == ?            
            """,
            (id, )
        )
        conn.commit()


def get_event_by_name(name_event: str) -> list[Any]:
    """
    События get_event_by_name. Находит событие по ИД.
    :param name_event: Название события
    :return: результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_events 
            WHERE name_event == ?            
            """,
            (name_event, )
        )
        events = cursor.fetchall()
        return events


def check_participation(id_user: int, id_event: int) -> list[Any]:
    """
    Функция check_participation.
    Проверяет, участвует ли пользователь в данном событии
    :param id_user: ИД пользователя
    :param id_event: ИД события
    :return: результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_part_and_comm
            WHERE id_telegram == ? AND id_event = ?;
            """,
            (id_user, id_event, )
        )
        rec_row = cursor.fetchall()
        return rec_row


def del_participation(id_student:int, id_event:int) -> None:
    """
    Функция del_participation. Удаляет участника из события.
    :param id_student: ИД студента
    :param id_event: ИД события
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM table_part_and_comm 
            WHERE id_telegram == ? AND id_event == ?
            """,
            (id_student, id_event, )
        )
        conn.commit()


def add_participation(id_user: int, id_event: int, comment: str="None") -> None:
    """
    Функция add_participation. Добавляет участника к событию.
    :param id_user: ИД пользователя
    :param id_event: ИД события
    :param comment: Комментарий пользователя
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO table_part_and_comm(id_telegram, id_event, comment) VALUES (?, ?, ?);
            """,
            (id_user, id_event, comment, )
        )
        conn.commit()


def qty_part_event(id_event: int) -> list[Any]:
    """
    Функция qty_part_event. Подсчитывает количество участников в событии.
    :param id_event: ИД события
    :return: Результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT COUNT()
            FROM table_part_and_comm
            WHERE id_event == ?;
            """,
            (id_event, )
        )
        qty_part = cursor.fetchall()
        return qty_part


def get_detail_event(id_event: int) -> list[Any]:
    """
    Функция get_detail_event. Выдаёт детальную информацию о событии.
    :param id_event: ИД события
    :return: Результат поиска
    """
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT name_event, deadline, description, student_name, comment
            FROM table_events
                JOIN table_part_and_comm tpac on table_events.id = tpac.id_event
                JOIN table_users tu on tu.telegram_id = tpac.id_telegram
            WHERE id_event == ?;
            """,
            (id_event, )
        )
        event = cursor.fetchall()
        return event


def create_password() -> str:
    """
    Функция create_password. Генерирует уникальный пароль.
    :return: Уникальный пароль
    """
    password = ""
    for i in range(8):
        letter = chr(random.randrange(97, 122))
        digital = chr(random.randrange(48, 55))
        sym = random.choices((letter, digital))
        password += sym[0]

    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM table_users
            WHERE password == ?
            """,
            (password, )
        )
        list_events = cursor.fetchall()

        if not list_events:
            return password
        else:
            create_password()

# 1115733873
