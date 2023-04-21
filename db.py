import time
import psycopg2
from psycopg2 import OperationalError

create_data_table = """
CREATE TABLE IF NOT EXISTS data (
  id SERIAL PRIMARY KEY,
  data TEXT NOT NULL, 
  date text NOT NULL)"""


def create_connection(db_name, db_user, db_password, db_host, db_port):
    "Создание подключения к БД"
    connection = None
    file = open('log.txt', 'a', encoding='utf-8')
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        file.write(f"{current_time} Успешное подключение к БД\n")
    except OperationalError as e:
        file.write(f"{current_time} Не удалось подключиться к БД\n")
    return connection


def execute_query(connection, query):
    "Выполнение запроса на добавление данных в БД"
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        file = open('log.txt', 'a', encoding='utf-8')
        file.write(f"{current_time} Запрос на добавление данных в таблицу выполнен успешно\n")
    except OperationalError as e:
        file = open('log.txt', 'a', encoding='utf-8')
        file.write(f"{current_time} {e} Не удалось выполнить запрос на добавление наддых в таблицу \n")


def execute_read_query(connection, query):
    "Выполнение запроса на чтение из БД"
    current_time = time.strftime("%m/%d/%Y %H:%M:%S")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        file = open('log.txt', 'a', encoding='utf-8')
        file.write(f"{current_time} Запрос на чтение выполнен успешно\n")
        return result
    except OperationalError as e:
        file = open('log.txt', 'a', encoding='utf-8')
        file.write(f"{current_time} {e} Не удалось выполнить запрос на чтение\n")
