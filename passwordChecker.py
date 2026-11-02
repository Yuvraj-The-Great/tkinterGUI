import sqlite3
import bcrypt

# database connections
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# database verification
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password BLOB)"
)

#checks username for password and username, if the combo exists returns true
def passwordCheck(username,password):
    data = cursor.execute(
        "SELECT password FROM users WHERE username=?", (username,)
    )
    
    rows = data.fetchone()

    if rows:
        #checks if user input matches db hash
        print(bcrypt.checkpw(password.encode("utf-8"), rows[0]))
        return (bcrypt.checkpw(password.encode("utf-8"), rows[0]))

    else:
        return False

#adds username and password combo to db
def passwordInsert(username,password):
    b4check = cursor.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone() #see if one exists
    
    if (b4check) is None:
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()) #salting
        cursor.execute("INSERT INTO users(username,password) VALUES (?,?)", (username, hashed)) #inserts hased favlue into db
        connection.commit()
        return True

    else:
        return False
