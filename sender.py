import time
from string import ascii_lowercase
from random import sample
from db import *


def main():
    "Подключение к БД"
    connection = create_connection("pgdb", "oleg", "123456", "192.168.1.74", "5432")

    "Создание таблицы в БД если ее не существует"
    execute_query(connection, create_data_table)

    while True:
        time.sleep(2)
        "Получение количества записей в БД"
        query_last_id = "SELECT id FROM data;"
        last_id = execute_read_query(connection, query_last_id)
        "Если записей больше 30, чистим таблицу и сбрасываем инкримент"
        if len(last_id) > 30:
            query_delete_data = (f"DELETE FROM data")
            query_reset_inc = (f"TRUNCATE TABLE data RESTART IDENTITY")
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(query_delete_data)
            cursor.execute(query_reset_inc)
            file.write(f"Очистка таблицы прошла успешно\n")

        "Запись в переменную текущего времени"
        current_time = time.strftime("%m/%d/%Y %H:%M:%S")

        "Генерация случайного слова для формирования разных данных"
        word = ''.join(sample(ascii_lowercase, 10)).capitalize()

        "Формирование корежа для передачи в запрос на добавление данных"
        data = (word, current_time)

        "Формирование запроса для добавления данных в таблицу"
        insert_query = (f"INSERT INTO data (data, date) VALUES {data}")
        connection.autocommit = True

        "Вызов метода для выполнения запроса в БД"
        execute_query(connection, insert_query)
        "Логирование работы скрипта в файл"
        file = open('log.txt', 'a', encoding='utf-8')
        file.write(f"Запись данных в БД прошла успешно. Добавлена запись: {word} в {current_time}\n")


if __name__ == '__main__':
    main()
