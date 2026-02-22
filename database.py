import sqlite3
import os

DB_PATH = "./data/shoppinglist.db"

def exist_db():

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lists (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            list_number INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                FOREIGN KEY (list_id) references lists(id)
        )
    ''')

    conn.commit()

    conn.close()



def create_list():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT MAX(list_number) FROM lists
    ''')

    result = cursor.fetchone()[0]

    next_number = 1 if result is None else result + 1
    cursor.execute("INSERT INTO lists (list_number) VALUES (?)", (next_number,))

    new_list_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return new_list_id, next_number