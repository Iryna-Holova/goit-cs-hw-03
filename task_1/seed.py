from faker import Faker
from random import randint
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

STATUS = [('new',), ('in progress',), ('completed',)]
NUMBER_USERS = 50
NUMBER_TASKS = 100


def generate_fake_data(
    number_users, number_tasks, number_status
) -> tuple:
    fake = Faker()
    fake_users = []
    fake_tasks = []

    for _ in range(number_users):
        fake_users.append((fake.name(), fake.free_email()))

    for _ in range(number_tasks):
        status_id = randint(1, number_status)
        user_id = randint(1, number_users)
        fake_tasks.append((fake.sentence(), fake.text(), status_id, user_id))

    return fake_users, fake_tasks


def truncate_tables(cursor):
    cursor.execute("TRUNCATE TABLE tasks CASCADE;")
    cursor.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE status RESTART IDENTITY CASCADE;")


def insert_data_to_db(status, users, tasks) -> None:
    with psycopg2.connect(
        database=DB_NAME,
        host="localhost",
        user=DB_USER,
        password=DB_PASSWORD,
        port=5432
    ) as conn:
        cursor = conn.cursor()
        truncate_tables(cursor)

        sql_to_status = """INSERT INTO status(name) VALUES (%s)"""
        cursor.executemany(sql_to_status, status)

        sql_to_users = """INSERT INTO users(fullname, email) VALUES (%s, %s)"""
        cursor.executemany(sql_to_users, users)

        sql_to_tasks = """INSERT INTO tasks(
                            title, description, status_id, user_id
                        )
                            VALUES (%s, %s, %s, %s)"""
        cursor.executemany(sql_to_tasks, tasks)

        conn.commit()


if __name__ == "__main__":
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS, len(STATUS))
    insert_data_to_db(STATUS, users, tasks)
