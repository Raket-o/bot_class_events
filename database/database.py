""" Модуль работы с базой данных"""

import sqlite3
import json


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
            INSERT INTO table_users (student_name, password) VALUES ("Admin", "Admin")
            """
        )
    conn.commit()


def check_password(*args):
    try:
        student_name, password = args[0][0], args[0][1]
    except IndexError:
        return None

    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id
            FROM table_users
            WHERE student_name == ? AND password == ?
            """,
            (student_name, password)
        )
        check_pass = cursor.fetchone()
        return check_pass


def update_info_for_db(telegram_id, user_first_name, user_last_name, id_student):
    print(id_student)

    with sqlite3.connect('database/database.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE table_users
            SET telegram_id = ?, user_first_name = ?, user_last_name = ?
            WHERE student_name = ?;
            """,
            (telegram_id, user_first_name, user_last_name, id_student)
        )


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
    init_db()