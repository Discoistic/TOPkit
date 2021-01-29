class actionsequence():
    def __init__(   self,
                    formatversion="2.6",
                    exportdate=832217040,
                    name=" -- ",
                    description=" -- ",
                    structurename=" -- "):
        self.formatversion = formatversion
        self.export = export

class variable:
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
    # def __repr__(self):
    #     return f"{self.name} = {self.value}"

    #Function that updates variable
    def update(self, name, value):
        self.name = name
        self.value = value

    #Spit out variable in json style with necessary checks
    def to_json(self):
        if isinstance(self.name, str) and isinstance(self.name, str):
            return '{\n\t"name": "'+self.name+'",\n\t"value": "'+self.value+'"\n}'
        else:
            raise("Both name and value must be a string")

class step():
    def __init__(self, name, method, url, escapebv, condition):
        self.name = name
        self.method = method
        pass

    def gen_headers(self):
        pass

class parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def remove(self):
        pass

    def update(self, name, value):
        self.name = name
        self.value = value
        return '"'+self.name+'": "'+self.value+'"'

    def nest(self, name, value):
        self._nested_name = name
        self._nested_value = value

        self.value =
        return '"'+self.name+'": "'+self.value+'"'

"body": "{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}"

def create(variables, parameters)

'''
print("{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}")
creates:
{
        "status": "firstLine",
        "callerLookup": {
                "email": "${aanmelderemail}"
        }
}
'''
