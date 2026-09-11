#sources:
#https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/
#https://docs.python.org/3/library/sqlite3.html

import sqlite3
import tkinter as tk
from tkinter import ttk

#database connections
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

#tkinter login window
root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")

main = ttk.Frame(root,relief="sunken",borderwidth=3)
main.pack(anchor="center",padx=20,pady=20, expand=True)

def logIn():
        print("YEY")

def signUp():
        print("no")
login = ttk.Button(main, text="Login", command=logIn())
login.pack()

sign = ttk.Button(main, text="Sign Up", command=signUP())
sign.pack()


root.mainloop()
