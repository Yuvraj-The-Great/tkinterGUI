import tkinter
from tkinter import ttk

print("Hello world")

#tkinter root window definition

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Robot GUI")
root.geometry("1920x1080")  # Width x Height

#frame 1
topLeft = ttk.Frame(root, borderwidth=50,relief='sunken')
topLeft.grid(row=0,column=0,sticky="nsew")

text = ttk.Label(topLeft, text = "Momomomm")
text.pack(expand=True)

#frame 2
topRight = ttk.Frame(root, borderwidth=50,relief='sunken')
topRight.grid(row=0,column=1,sticky="nsew")

text2 = ttk.Label(topRight, text = "Momomomm")
text2.pack(expand=True)

#frame 3
bottomLeft = ttk.Frame(root, borderwidth=50,relief='sunken')
bottomLeft.grid(row=1,column=0,sticky="nsew")

text3 = ttk.Label(bottomLeft, text = "Momomomm")
text3.pack(expand=True)

#frame 4
bottomRight = ttk.Frame(root, borderwidth=50,relief='sunken')
bottomRight.grid(row=1,column=1,sticky="nsew")

text4 = ttk.Label(bottomRight, text = "Momomomm")
text4.pack(expand=True)

#column and row configurations for sizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#mainloop must be at end
root.mainloop()