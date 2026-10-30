#sources: https://www.pythontutorial.net/tkinter/tkinter-grid/
#https://tkinterdocs.online/#
#https://docs.python.org/3/library/tkinter.html

#Pillow library transforming image to fit and rotating, needed to pip install pillow
#https://pillow.readthedocs.io/en/stable/reference/ImageTransform.html
#https://pillow.readthedocs.io/en/stable/reference/Image.html
#https://pillow.readthedocs.io/en/stable/reference/ImageTk.html Works with tkinter

#raspberry pi url
pi_url = "127.0.0.1"
import requests

#forward when the up button is pressed
def up():
    try:
        #Sends a JSON message to Raspi to Forward
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "forward"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"

    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
    
#backward when the down button is clicked
def down():
    try:
        #Sends a JSON message to Raspi to Backward
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "backward"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:    
        print("Failed")
        return "Failed"

#right when the right button is clicked
def right():
    try:
        #Sends a JSON message to Raspi to Right
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "right"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
    
#left when the left button is clicked
def left():
    try:
        #Sends a JSON message to Raspi to Left
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "left"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"
        
#play when the play button is clicked
def play():
    try:
        #Sends a JSON message to Raspi to Play
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "play"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"

    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"

#stop when the stop button is clicked
def stop():
    try:
        #Sends a JSON message to Raspi to Stop
        response = requests.post(
            f"{pi_url}/command",
            json={"action": "stop"},
            timeout=3
        )
        response.raise_for_status()

        print("Success")
        return "Success"
        
    #Returns the error message
    except requests.RequestException:
        print("Failed")
        return "Failed"

def startGUI():

    from PIL import Image #for resizing and rotating arrow images to meet test
    from PIL import ImageTk #for converting to tk file

    import tkinter
    from tkinter import ttk
    import tkinter as tk

    #login db
    import sqlite3

    connection = sqlite3.connect("users.db")
    conCur = connection.cursor()

    #tkinter root window definition
    root = tk.Tk()
    root.title("Tkinter Robot GUI")
    root.geometry("900x800")  # Width x Height

    #frame 1 (video)
    topLeft = ttk.Frame(root,relief='sunken')
    topLeft.grid(row=0,column=0,sticky="nsew")

    text = ttk.Label(topLeft, text = "Video Placeholder One")
    text.pack(expand=True)

    #frame 2 (controls)
    topRight = ttk.Frame(root,relief='sunken')
    topRight.grid(row=0,column=1,sticky="nsew")

    #buffer frame for centering
    topRightInner = ttk.Frame(topRight)
    topRightInner.pack(anchor="center",expand= True)

    #controls

    #arrow photo resizing and rotating with pillow
    arrowImage = None 
    with Image.open("arrow.png") as arrowRaw:
        arrowImage = arrowRaw.resize((70,50)) 

        #north south east west
        arrowImage1 = arrowImage.rotate(90, expand=True) #expand very important, expands image canvas to new size
        arrowImage2 = arrowImage.rotate(270, expand = True)
        arrowImage3 = arrowImage.rotate(180, expand = True)

    arrowPhoto = ImageTk.PhotoImage(arrowImage)

    #conversion from pil image to tkinter system
    arrowPhoto1 = ImageTk.PhotoImage(arrowImage1)
    arrowPhoto2 = ImageTk.PhotoImage(arrowImage2)
    arrowPhoto3 = ImageTk.PhotoImage(arrowImage3)
    arrowPhoto4 = ImageTk.PhotoImage(arrowImage)

    #pause and play button resizing and conversion to Tkinter image
    pausePhoto = None
    playPhoto = None

    with Image.open("pause_button.png") as pauseRaw:
        pauseRaw = pauseRaw.resize((65,65))
        pausePhoto = ImageTk.PhotoImage(pauseRaw)

    with Image.open("play_button.png") as playRaw:
        playRaw = playRaw.resize((65,65))
        playPhoto = ImageTk.PhotoImage(playRaw)

    arrow1 = tk.Button(topRightInner,command=up,image=arrowPhoto1) #north
    arrow1.grid(columnspan=2,column=1,row=0, padx=10, pady= 10, ipadx=5, ipady=5)

    arrow2 = tk.Button(topRightInner, command=right, image=arrowPhoto3) #east
    arrow2.grid(column=0,row=1, padx=10, pady= 10, ipadx=5, ipady=5)

    stopImage = None
    stopButton = tk.Button(topRightInner, command=stop, image=pausePhoto) 
    stopButton.grid(column=1,row=1, padx=10, pady= 10, ipadx=5, ipady=5)

    startImage = None
    startButton = tk.Button(topRightInner, command=play, image=playPhoto)
    startButton.grid(column=2,row=1, padx=10, pady= 10, ipadx=5, ipady=5)

    arrow3 = tk.Button(topRightInner, command=left,image=arrowPhoto4) #west
    arrow3.grid(column=3,row=1, padx=10, pady= 10, ipadx=5, ipady=5)

    arrow4 = tk.Button(topRightInner, command=down,image=arrowPhoto2)
    arrow4.grid(columnspan=2,column=1,row=2, padx=10, pady= 10, ipadx=5, ipady=5) #south

    #column and row configurations for sizing again :(
    topRightInner.grid_rowconfigure(0, weight=1)
    topRightInner.grid_rowconfigure(1, weight=1)

    topRightInner.grid_columnconfigure(0, weight=1)
    topRightInner.grid_columnconfigure(1, weight=1)
    topRightInner.grid_columnconfigure(2, weight=1)
    topRightInner.grid_columnconfigure(3, weight=1)

    #frame 3 (video)
    bottomLeft = ttk.Frame(root, padding=10,relief='sunken')
    bottomLeft.grid(row=1,column=0,sticky="nsew")

    text3 = ttk.Label(bottomLeft, text = "Video Placeholder Two")
    text3.pack(expand=True)

    #frame 4
    bottomRight = ttk.Frame(root,relief='sunken')
    bottomRight.grid(row=1,column=1,sticky="nsew")

    centerbottomRight = ttk.Frame(bottomRight)
    centerbottomRight.pack(anchor="center",pady=(30,0)) #could not get this to auto center apart from manually
                                                        #setting pady

    text4 = ttk.Label(centerbottomRight, text = "User Log Placeholder")
    text4.pack(pady=(30,30))

    userLog = tk.Text(centerbottomRight,width=40,height=10)
    userLog.pack(pady=(0,30))

    #column and row configurations for sizing
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    1

    #mainloop must be at end
    root.mainloop()
