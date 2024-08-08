import sqlite3

class UserDB:

    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path

    def _create_connection(self):
        return sqlite3.connect(self.db_path)
        
    def create_user(self, document: str, credit_card: str) -> bool:
        conn = self._create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (userDocument, creditCardToken) VALUES (?, ?)", (
            document, credit_card
        ))
        conn.commit()
        conn.close()
        return True