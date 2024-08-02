import psycopg2
from dotenv import load_dotenv
import os
import sys

def save_review(company, product, vendor_code, pros, cons, comment, grade):
    # Проверяем, запущено ли приложение из исполняемого файла, созданного PyInstaller
    if getattr(sys, 'frozen', False):
        # Если приложение запущено из исполняемого файла, используем временную папку PyInstaller
        dotenv_path = os.path.join(sys._MEIPASS, '.env')
        load_dotenv(dotenv_path)
        # print('Запущен из скомпилированного файла')
    else:
        # В противном случае, используем стандартный путь
        print('Запущен интерпреатор ')
        load_dotenv()
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    try:
        conn = psycopg2.connect(
            host= POSTGRES_HOST,
            port= POSTGRES_PORT,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            options='-c client_encoding=UTF8'  # Указание кодировки соединения
        )
        cur = conn.cursor()
        sql = "INSERT INTO reviews (company, product, vendor_code, pros, cons, comment, grade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (company, product, vendor_code, pros, cons, comment, grade)
        print(values)
        cur.execute(sql, values)
        conn.commit()

        print("Данные успешно сохранены!")

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)

    finally:
        if conn:
            cur.close()
            conn.close()