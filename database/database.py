import sqlite3 

def create_connection():
    connection = None
    connection = sqlite3.connect("database.db")
    return connection

def create_table():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userDocument TEXT NOT NULL UNIQUE,
                creditCardToken TEXT NOT NULL UNIQUE,
                value INTEGER
            );
        """
        )

        connection.commit()
    except sqlite3.Error as database_error:
        print(f"O erro {database_error} ocorreu")
    finally:
        connection.close()


