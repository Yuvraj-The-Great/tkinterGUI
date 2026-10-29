#sources:
#https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/
#https://docs.python.org/3/library/sqlite3.html

#database checking: https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists

#https://www.geeksforgeeks.org/sqlite/sqlite-autoincrement/ 

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#command arguments for button
from functools import partial

#importing the tkinter GUI 
from tkinterGUI import startGUI

#database connections
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

#database verification
cursor.execute("CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

#tkinter login window
root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200+200+200")

main = ttk.Frame(root,relief="sunken",borderwidth=3)
main.pack(anchor="center",padx=20,pady=20, expand=True,ipadx=20,ipady=20)

def logIn():
        def logCheck(username,password):
                username = username.get()
                password = password.get()
                
                data = cursor.execute("SELECT * FROM users WHERE username=? and password=?",(username,password))
                rows = data.fetchone()

                if rows:
                        logInWindow.destroy()
                        root.destroy()
                        startGUI()

                else:
                        messagebox.showerror("Error","Login Failed, Create a New Account!")
                        logInWindow.destroy()

        logInWindow = tk.Toplevel(root)
        logInWindow.geometry("300x200")
        logInWindow.title("Log In")
        logInWindow.grab_set()

        mainLogin = ttk.Frame(logInWindow,relief="sunken",borderwidth=3)
        mainLogin.pack(anchor="center",padx=20,pady=20, expand=True,ipadx=20,ipady=20)

        #username field and variable
        username = tk.StringVar(value="Username Field")
        usernameEntry = tk.Entry(mainLogin, textvariable=username)
        usernameEntry.pack(anchor="center",pady=(20,0))

        password = tk.StringVar(value="Password Field")
        passwordEntry = tk.Entry(mainLogin, textvariable=password, show="*") #show hides password while typing
        passwordEntry.pack(anchor="center")

        logCheckPartial = partial(logCheck,username,password)

        enterButton = tk.Button(mainLogin, text="Enter",command=logCheckPartial)
        enterButton.pack(anchor="center",expand=True,fill="x",padx=20)

def signUp():
        def signCheck(username,password):
                username = username.get()
                password = password.get()

                check = cursor.execute("SELECT * FROM users WHERE username=?",(username,))

                if (check is not None):
                        cursor.execute("INSERT INTO users(username,password) VALUES (?,?)",(username, password))
                        connection.commit()
                        messagebox.showinfo("Done","New Account Created!")

                        signUpWindow.destroy()
                else: 
                        messagebox.showerror("Username Errors","Username already exists!")
                        signUpWindow.destroy()


        signUpWindow = tk.Toplevel(root)
        signUpWindow.geometry("300x200")
        signUpWindow.title("Create Account")
        signUpWindow.grab_set()

        mainSignUp = ttk.Frame(signUpWindow,relief="sunken",borderwidth=3)
        mainSignUp.pack(anchor="center",padx=20,pady=20, expand=True,ipadx=20,ipady=20)

        #username field and variable
        username = tk.StringVar(value="Username Field")
        usernameEntry = tk.Entry(mainSignUp, textvariable=username)
        usernameEntry.pack(anchor="center",pady=(20,0))

        password = tk.StringVar(value="Password Field")
        passwordEntry = tk.Entry(mainSignUp, textvariable=password, show="*") #show hides password while typing
        passwordEntry.pack(anchor="center")

        signCheckPartial = partial(signCheck,username,password)

        enterButton = tk.Button(mainSignUp, text="Enter",command=signCheckPartial)
        enterButton.pack(anchor="center",expand=True,fill="x",padx=20)
        

login = ttk.Button(main, text="Login", command=logIn)
login.pack(pady=(30,0))

sign = ttk.Button(main, text="Create Account", command=signUp)
sign.pack()

root.mainloop()
logIn()
