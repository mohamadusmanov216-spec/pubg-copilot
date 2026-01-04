from bot.database.db import get_connection


def get_profile(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT profile_text FROM profiles WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()

    conn.close()
    return row["profile_text"] if row else None


def create_profile(user_id: int, text: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO profiles (user_id, profile_text) VALUES (?, ?)",
        (user_id, text)
    )

    conn.commit()
    conn.close()


def update_profile(user_id: int, text: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE profiles SET profile_text = ? WHERE user_id = ?",
        (text, user_id)
    )

    conn.commit()
    conn.close()

