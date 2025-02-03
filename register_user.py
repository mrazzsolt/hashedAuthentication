import hashlib
import sqlite3

DB_NAME = "credentials.db"

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def is_username_taken(self, username):
        self.c.execute("SELECT username FROM users WHERE username = ?", (username,))
        return self.c.fetchone() is not None

    def register_user(self, username, password):
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database(DB_NAME)

    print("Registration")
    while True:
        username = input("Username: ")
        if db.is_username_taken(username):
            print("Invalid username. Please choose another one!")
        else:
            break

    password = input("Password: ")
    db.register_user(username, password)
    print("Registration was successful.")

    db.close_connection()
