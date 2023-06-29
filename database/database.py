""" Модуль работы с базой данных"""

import sqlite3
import json
import random


def init_db() -> None:
    """ Функция init_db. При отсутствии базы донной создаёт ёё. """
    with sqlite3.connect('database/database.db') as conn:
    # with sqlite3.connect('database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
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
                description TEXT DEFAULT NULL,
                id_participants INTEGER
            )
            """
        )
    # else:
    #     cursor.execute("DROP TABLE table_events;")


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
                blocked BOOL DEFAULT False
            )
            """
        )
    # else:
    #     cursor.execute("DROP TABLE table_users;")

        cursor.execute(
            """
            INSERT INTO table_users (student_name, password) VALUES ("1", "1")
            """
        )
    conn.commit()


def check_users(name):
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


def check_password(student_name, password):
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


def update_info_for_db(telegram_id, user_first_name, user_last_name, student_name):
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET telegram_id = ?, user_first_name = ?, user_last_name = ?
            WHERE student_name = ?;
            """,
            (telegram_id, user_first_name, user_last_name, student_name)
        )
        conn.commit()

def get_evets():
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


def gets_students():
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


def add_student(name_student):
    password = create_password()
    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO table_users (student_name, password) VALUES (?, ?);
            """,
            (name_student, password, )
        )
        list_users = cursor.fetchall()
        conn.commit()
        return list_users


def check_users_by_id(id):
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
        id_user = cursor.fetchone()
        return id_user


def edit_users_by_id(id, name):
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


def reset_password_users_by_id(id:int) -> str:
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


def del_users_by_id(id:int) -> str:
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


def blocked_users_by_id(id:int, status:bool) -> str:
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


def create_password():
    password = ""
    for i in range(8):
        letter = chr(random.randrange(97, 122))
        digital = chr(random.randrange(48, 55))
        sym = random.choices((letter, (digital)))
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





    # SET telegram_id = {telegram_id}, user_first_name = {user_first_name}, user_last_name = {user_last_name}

    # cursor.execute('''UPDATE books SET price = ? WHERE id = ?''', (newPrice, book_id))


    # if not exists:
    #     cursor.executescript(
    #         """
    #         CREATE TABLE `table_events` (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             user_id INTEGER DEFAULT 0,
    #             user_name TEXT DEFAULT NULL,
    #             command TEXT DEFAULT NULL,
    #             country TEXT DEFAULT NULL,
    #             city TEXT DEFAULT NULL,
    #             city_area TEXT DEFAULT NULL,
    #             list_hotels TEXT DEFAULT NULL,
    #             method_sort TEXT DEFAULT NULL
    #         )
    #         """
    #     )
    # conn.commit()


# def rec_cmd_low(dict_data) -> None:
#     """ Функция rec_cmd_low. Записывает данные в базу данных"""
#     with sqlite3.connect('database/database.db') as conn:
#         cursor: sqlite3.Cursor = conn.cursor()
#         cursor.execute(
#             """
#             INSERT INTO table_user_request (user_id, user_name, command, country, city, city_area, list_hotels, method_sort)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#             """,
#             (
#                 dict_data["user_id"],
#                 dict_data["user_name"],
#                 dict_data["command"],
#                 dict_data["country"],
#                 dict_data["city"],
#                 dict_data["city_area"],
#                 json.dumps(dict_data["list_hotels"]),
#                 dict_data["method_sort_for_history"]
#             )
#         )
#         conn.commit()
#
#
# def seek_history(user_id: int):
#     """
#     Функция seek_history. Находит по user_id и возвращает строки из бд.
#     :param user_id: Ид пользователя
#     :return: список[со строками из бд]
#     """
#     with sqlite3.connect('database/database.db') as conn:
#         cursor: sqlite3.Cursor = conn.cursor()
#         cursor.execute(
#             """
#             SELECT *
#             FROM table_user_request WHERE user_id = ?
#             """,
#             (user_id, )
#         )
#         detail_history = cursor.fetchall()
#
#         return detail_history
#
#
# def delete_history_db(user_id: int) -> None:
#     """
#     Функция delete_history_db. Принимает на вход user_id
#     и удаляет все строки с данным user_id
#     :param user_id: user_id
#     :return: None
#     """
#     with sqlite3.connect('database/database.db') as conn:
#         cursor: sqlite3.Cursor = conn.cursor()
#         cursor.execute(
#             """
#             DELETE FROM table_user_request WHERE user_id = ?
#             """,
#             (user_id, )
#         )

if __name__ == "__main__":
    # init_db()

    print(create_password())

