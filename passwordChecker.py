import sqlite3
import bcrypt

# database connections
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# database verification
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
)


def passwordCheck(username,password):
    data = cursor.execute(
        "SELECT * FROM users WHERE username=? and password=?", (username, password)
    )
    
    rows = data.fetchone()

    if rows:
        return rows

    else:
        return False
