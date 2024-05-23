import psycopg2
from dotenv import load_dotenv
import os
def save_review(product, vendor_code, pros, cons, comment, grade):
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
            password=POSTGRES_PASSWORD
        )
        cur = conn.cursor()
        sql = "INSERT INTO reviews (product, vendor_code, pros, cons, comment, grade) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (product, vendor_code, pros, cons, comment, grade)
        cur.execute(sql, values)
        conn.commit()

        print("Данные успешно сохранены!")

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)

    finally:
        if conn:
            cur.close()
            conn.close()