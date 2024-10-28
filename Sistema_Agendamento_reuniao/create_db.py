import sqlite3

def create_database():
    conn = sqlite3.connect('meetings.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_database()
