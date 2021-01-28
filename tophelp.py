import tkinter as tk
from tkinter import messagebox

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
