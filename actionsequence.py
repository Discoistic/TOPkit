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
