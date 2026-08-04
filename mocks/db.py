import sqlite3


def save_user(namee, age):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO (name, age) values (?, ?)", (namee,age))
    conn.commit()
    conn.close()