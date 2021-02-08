# Start with importing all necessary stuff
import tkinter as tk
import ctypes
import gui as ui
# import actionsequence as acts


# This piece of code mirrors the window icon to the taskbar icon
App = 'MerijnA_TOPkit_0.0.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(App)

# Create the main frame for the main menu
root = tk.Tk()

# Load the content of the main menu into the frame
App = ui.MainMenu(root)

# Make the application responsive 6by refreshing it over and over
root.mainloop()

# That's all it takes to make the heart of this application beat.
