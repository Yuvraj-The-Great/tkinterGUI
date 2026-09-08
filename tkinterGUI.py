#sources: https://www.pythontutorial.net/tkinter/tkinter-grid/
#https://tkinterdocs.online/#
#https://docs.python.org/3/library/tkinter.html

import tkinter
from tkinter import ttk

print("Hello world")

#tkinter root window definition

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Robot GUI")
root.geometry("1920x1080")  # Width x Height

#frame 1 (video)
topLeft = ttk.Frame(root, borderwidth=50,relief='sunken')
topLeft.grid(row=0,column=0,sticky="nsew")

text = ttk.Label(topLeft, text = "Video Placeholder 1")
text.pack(expand=True)

#frame 2 (controls)
topRight = ttk.Frame(root,relief='sunken')
topRight.grid(row=0,column=1,sticky="nsew")

#buffer frame for centering
topRightInner = ttk.Frame(topRight, borderwidth=50)
topRightInner.pack(anchor="center",expand= True)

#controls
arrowPhoto = None 
arrow1 = ttk.Button(topRightInner,image=arrowPhoto)
arrow1.grid(columnspan=2,column=1,row=0)

arrow2 = ttk.Button(topRightInner,image=arrowPhoto)
arrow2.grid(column=0,row=1)

stopImage = None
stopButton = ttk.Button(topRightInner, image=stopImage)
stopButton.grid(column=1,row=1)

startImage = None
startButton = ttk.Button(topRightInner, image=startImage)
startButton.grid(column=2,row=1)

arrow3 = ttk.Button(topRightInner, image=arrowPhoto)
arrow3.grid(column=3,row=1)

arrow4 = ttk.Button(topRightInner, image=arrowPhoto)
arrow4.grid(columnspan=2,column=1,row=2)

#column and row configurations for sizing again :(
topRightInner.grid_rowconfigure(0, weight=1)
topRightInner.grid_rowconfigure(1, weight=1)

topRightInner.grid_columnconfigure(0, weight=1)
topRightInner.grid_columnconfigure(1, weight=1)
topRightInner.grid_columnconfigure(2, weight=1)
topRightInner.grid_columnconfigure(3, weight=1)

#frame 3 (video)
bottomLeft = ttk.Frame(root, padding=10,borderwidth=50,relief='sunken')
bottomLeft.grid(row=1,column=0,sticky="nsew")

text3 = ttk.Label(bottomLeft, text = "Video Placeholder One")
text3.pack(expand=True)

#frame 4
bottomRight = ttk.Frame(root,relief='sunken')
bottomRight.grid(row=1,column=1,sticky="nsew")

text4 = ttk.Label(bottomRight, text = "User Log Placeholder")
text4.pack(expand=True)

userLog = tk.Text(bottomRight)
userLog.pack(expand=True)

#column and row configurations for sizing
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#mainloop must be at end
root.mainloop()