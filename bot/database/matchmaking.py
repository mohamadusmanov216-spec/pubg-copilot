from bot.database.db import get_connection


def add_to_queue(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO matchmaking_queue (user_id) VALUES (?)",
        (user_id,)
    )

    conn.commit()
    conn.close()


def remove_from_queue(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM matchmaking_queue WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def find_match(user_id: int):
    """
    Ищет любого другого игрока в очереди.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id FROM matchmaking_queue WHERE user_id != ? LIMIT 1",
        (user_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        return user_id, row["user_id"]

    return None

