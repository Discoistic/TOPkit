# Start with importing all necessary stuff
import tkinter as tk
from tkinter import messagebox
import ctypes
#    _____             _
#   |  __ \           | |
#   | |__) |___   ___ | |_
#   |  _  // _ \ / _ \| __|
#   | | \ \ (_) | (_) | |_
#   |_|  \_\___/ \___/ \__|

class masterwindow:
    '''
    Creates the basic window and frame to fit standard information in.
    Should only be used for settings used everywhere.
    '''
    def __init__(self, root_var):
        # Set the default window options
        self.root_var = root_var
        self.root_var.iconbitmap(r'icon.ico')  # Dit werkt niet
        self.root_var.geometry("500x150")
        self.root_var.lift()

        # Create a consistent header everywhere
        self.header_frame = tk.Frame(root_var)
        self.header_frame.pack()

        header = tk.Label(self.header_frame,
                          text="Do not share with clients!",
                          font="impact")
        header.pack()



class MainMenu(masterwindow):
    '''
    Creates the main menu. Requires a direct definition of the root/master window.
    '''
    def __init__(self, root_var):
        self.root_var = root_var
        super().__init__(root_var)

        self.frame = tk.Frame(root_var)
        self.frame.pack()

        self.root_var.title("MerijnA's TOPkit")

        self.btn_tophelp = tk.Button(self.frame, text="TOPhelp to My Topdesk", command=lambda: new_window())
        self.quitbutton = tk.Button(self.frame, text="Quit this tool", command=root_var.destroy)

        self.btn_tophelp.pack()
        self.quitbutton.pack()

    def new_window(self):
        self.new_root = tk.Toplevel(self.root_var)
        app = tophelp_window(self.new_root)
#    _______          _          _
#   |__   __|        | |        | |
#      | | ___  _ __ | |__   ___| |_ __
#      | |/ _ \| '_ \| '_ \ / _ \ | '_ \
#      | | (_) | |_) | | | |  __/ | |_) |
#      |_|\___/| .__/|_| |_|\___|_| .__/
#              | |                | |
#              |_|                |_|
class tophelp_window(masterwindow):
    '''
    Creates the TOPhelp screen and URL changer functionality. Requires a direct definition of the root/master window.
    '''
    def __init__(self, root_var):
        super().__init__(root_var)
        self.root_var = root_var

        self.frame = tk.Frame(root_var)
        self.frame.pack()

        self.root_var.title("TOPhelp link changer")

        changer = tk.Button(self.root_var, text="Click to change url", command=self._urlchanger)
        changer_explanation = tk.Message(self.root_var, text="Reads last clipboard entry and if TOPhelp URL, changes to MyTOPdesk", )

        changer.pack()
        changer_explanation.pack()

    def _urlchanger(self):
        '''Change TOPhelp URL to My TOPdesk URL'''
        # First get the clipboard content
        # Gets a TOPhelp URL, such as https://tophelp.topdesk.com/tas/public/ssp/content/detail/knowledgeitem?unid=513caaea948e4b8a9e567c9ebbce60b4
        clipboard = self.root_var.clipboard_get()

        # check for it being a KI hotlink
        if "https://tophelp.topdesk.com/" in clipboard and len(clipboard) < 150:
            mytopdeskurl = clipboard.replace("https://tophelp.topdesk.com/", "https://my.topdesk.com/")
            self.root_var.clipboard_clear()
            self.root_var.clipboard_append(mytopdeskurl)
        else:
            messagebox.showerror(title="Not a (valid) TOPhelp URL", message="To make this work, the URL must at least contain https://tophelp.topdesk.com/ and be less than 150 chars long. Please try again.")
            self.root_var.lift()

#                 _   _                _____
#       /\       | | (_)              / ____|
#      /  \   ___| |_ _  ___  _ __   | (___   ___  __ _ _   _  ___ _ __   ___ ___
#     / /\ \ / __| __| |/ _ \| '_ \   \___ \ / _ \/ _` | | | |/ _ \ '_ \ / __/ _ \
#    / ____ \ (__| |_| | (_) | | | |  ____) |  __/ (_| | |_| |  __/ | | | (_|  __/
#   /_/    \_\___|\__|_|\___/|_| |_| |_____/ \___|\__, |\__,_|\___|_| |_|\___\___|
#                                                    | |
#                                                    |_|
class actionsequence():
    def __init__(self, formatversion="2.6", export=832217040,  ):
        self.formatversion = formatversion
        self.export = export



class as_variable:
    '''

    Creates an action sequence variable. \n
    Takes: \n
    \t    'Name': The name that is shown in the left column
    \t    'Value': The description/entry that is given in the right column \n

    Functions: \n
    \t    '.update()': updates the variable with name and/or a value
    \t    '.to_json()': returns(!) out a pre-formatted json friendly variable. \n

    Examples: \n
    \t    'vr_td_usr = as_variable(name="topdesk_user", value="Enter in your API user here")'
    \t    'vr_td_usr.update(name="topdesk_user", value=tk.e.get())' #fills value with tkinter entry
    \t    'vr_td_usr.json()' #spits out a json formatted line of code

    '''
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"{self.name} = {self.value}"

    #Function that updates variable
    def update(self, name, value):
        self.name = name
        self.value = value

    #Spit out variable in json style with necessary checks
    def to_json(self):
        if isinstance(self.name, str) and isinstance(self.name, str):
            return '{\n\t"name": "'+self.name+'",\n\t"value": "'+self.value+'"\n}'
        else:
            print("Both name and value must be a string")
    def to_var(self):
        pass

class step():
    def __init__(self, name, method, url, escapebv, condition):
        self.name = name
        self.method = method
        pass

    def gen_headers(self):
        pass

class parameter:
    def __init__(self):
        pass

    def add_to_step(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass

    def nest(self, dict):
        pass


print("{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}")
'''
{
        "status": "firstLine",
        "callerLookup": {
                "email": "${aanmelderemail}"
        }
}
'''

# This piece of code mirrors the window icon to the taskbar icon
App = 'MerijnA_TOPkit_0.0.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(App)

# Create the main frame for the main menu
root = tk.Tk()

# Load the content of the main menu into the frame
App = MainMenu(root)

# Make the application responsive by refreshing it over and over
root.mainloop()

# That's all it takes to make the heart of this application beat. Now time to make it function.
