import sqlite3
import os

DB_PATH = "database.db"


def get_connection():
    """
    Возвращает подключение к базе данных.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Создаёт таблицы, если их нет.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Таблица профилей игроков
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            user_id INTEGER PRIMARY KEY,
            profile_text TEXT
        )
    """)

    # Очередь матчмейкинга
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matchmaking_queue (
            user_id INTEGER PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()

