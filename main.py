#import log in window
from tkinterLogin import logInGUI

# importing the tkinter GUI
from tkinterGUI import startGUI

print("Login GUI started.")
success = logInGUI()

if success:
  print("Started main GUI, login success.")
  startGUI()
