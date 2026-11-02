#import log in window
from tkinterLogin import logInGUI

# importing the tkinter GUI
from tkinterGUI import startGUI

success = logInGUI()

if success:
  startGUI()
