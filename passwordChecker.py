import sqlite3
import bcrypt

# database connections
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# database verification
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
)

#checks username for password and username, if the combo exists returns true
def passwordCheck(username,password):
    data = cursor.execute(
        "SELECT * FROM users WHERE username=? and password=?", (username, password)
    )
    
    rows = data.fetchone()

    if rows:
        return True

    else:
        return False

#adds username and password combo to db
def passwordInsert(username,password):
    b4check = cursor.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone() #see if one exists
    
    if (b4check) is None:
        cursor.execute("INSERT INTO users(username,password) VALUES (?,?)", (username, password))
        connection.commit()
        return True

    else:
        return False
        
