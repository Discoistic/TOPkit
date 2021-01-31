# Start with importing all necessary stuff
import tkinter as tk
from tkinter import messagebox
import ctypes
import tophelp as th
import actionsequence as ac
# import actionsequence as acts

# Create
class MainMenu:
    '''
    Creates the main menu. Requires a direct definition of the
    root/master window.
    '''
    def __init__(self, root_var):
        self.root_var = root_var
        self.root_var.iconbitmap(r'icon.ico')  # Dit werkt niet
        self.root_var.geometry("500x150")
        self.root_var.lift()

        # Create a consistent header everywhere
        self.frame = tk.Frame(root_var)
        self.frame.pack()
        self.header = tk.Label(self.frame,
                          text="Do not share with clients!",
                          font="impact")
        self.header.pack()

        self.root_var.title("MerijnA's TOPkit")

        self.btn_tophelp = tk.Button(self.frame, text="TOPhelp to My Topdesk",
                                    command=self.new_window)
        self.quitbutton = tk.Button(self.frame, text="Quit this tool",
                                    command=root_var.destroy)

        self.btn_tophelp.pack()
        self.quitbutton.pack()

    def new_window(self):
        self.new_root = tk.Toplevel(self.root_var)
        app = th.tophelp_window(self.new_root)


# This piece of code mirrors the window icon to the taskbar icon
# App = 'MerijnA_TOPkit_0.0.1'
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(App)

# Create the main frame for the main menu
root = tk.Tk()

# Load the content of the main menu into the frame
App = MainMenu(root)

# Make the application responsive by refreshing it over and over
root.mainloop()

# That's all it takes to make the heart of this application beat.
