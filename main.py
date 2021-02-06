# Start with importing all necessary stuff
import tkinter as tk
# import ctypes
import gui as ui
# import actionsequence as acts


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
        self.frame.grid()
        self.header = tk.Label(self.frame,
                               text="Do not share with clients!",
                               font="impact")
        self.header.grid()

        self.root_var.title("MerijnA's TOPkit")

        self.btn_tophelp = tk.Button(self.frame, text="TOPhelp to My Topdesk",
                                     command=self.tophelp_window)
        self.btn_as = tk.Button(self.frame, text="Action Sequence builder",
                                command=self.as_window)
        self.quitbutton = tk.Button(self.frame, text="Quit this tool",
                                    command=root_var.destroy)

        self.btn_tophelp.grid()
        self.btn_as.grid()
        self.quitbutton.grid()

    def tophelp_window(self):
        self.new_root = tk.Toplevel(self.root_var)
        ui.tophelp_window(self.new_root)

    def as_window(self):
        ui.as_window(self.root_var)


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
