import hashlib
import sqlite3

DB_NAME = "credentials.db"

def credentials_validation(username,password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    credentials = c.execute("""
        SELECT *
        FROM users
        WHERE
          username = ? AND
          password = ?
    """, (username, password_hash)).fetchone()

    return credentials is not None

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")

    if credentials_validation(username,password):
        print("Successful login!")
    else:
        print("Invalid credentials!")