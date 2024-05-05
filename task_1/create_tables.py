import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def create_db():
    try:
        with open('create_tables.sql', 'r') as file:
            sql = file.read()

        with psycopg2.connect(
            database=DB_NAME,
            host="localhost",
            user=DB_USER,
            password=DB_PASSWORD,
            port=5432
        ) as conn:
            cursor = conn.cursor()

            cursor.execute(sql)
            print("Database created successfully!")
    except psycopg2.Error as e:
        print("Error creating database:", e)


if __name__ == "__main__":
    create_db()
