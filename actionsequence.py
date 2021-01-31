import json

class actionsequence():
    def __init__(   self,
                    formatversion="2.6",
                    exportdate=832217040,
                    name=" -- ",
                    description=" -- ",
                    structurename=" -- "):
        self.formatversion = formatversion
        self.export = exportdate
        self.name = name
        self.description = description
        self.structurename = structurename
        self._variables = [] # Stores the variables. Crucial!
        self._steps = []

    def add_variable(self, variable):
        self._variables.append(variable)

    def reset_variables(self):
        self._variables = []

    def add_step(self, step):
        self._steps.append()

    def reset_steps(self, step):
        self._steps = []


    def build(self, variables):
        return { # level 1
        "formatversion": self.formatversion,
        "exportDate": self.exportdate,
        "actionSequence":{ # level 2
            "name": self.name,
            "description": self.description,
            "structureName": self.structurename,
            "configuration":{
                "variables": self._variables,
                "mappingDefinitions": [],
                "steps": self.steps
                }
            }
        }


class variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return {"name": self.name, "value": self.value}

    #Function that updates variable
    def update(self, name, value):
        self.name = name
        self.value = value

    #Spit out variable in json style with necessary checks
    # def to_json(self):
    #     if isinstance(self.name, str) and isinstance(self.name, str):
    #         return '{\n\t"name": "'+self.name+'",\n\t"value": "'+self.value+'"\n}'
    #     else:
    #         raise("Both name and value must be a string")

class step():
    def __init__(self, name, method, url, escape, condition):
        self.name = name
        self.method = method
        self.url = url
        self.secape = escape
        self.condition = condition
        self._headers = []

    def add_header(self, header):
        self._headers.append()

    def link_body

    def build(self):
        return {
        "name": self.name,
        "method": self.method,
        "url": self.url,
        "headers": self._headers,
        "escapeBodyValues": self.escape,
        "body": #FILL
        "executionCondition": self.condition,
        "customExecutionCondition": ""
        }

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


'''
"body": "{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}"

print("{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}")
creates:
{
        "status": "firstLine",
        "callerLookup": {
                "email": "${aanmelderemail}"
        }
}
'''
