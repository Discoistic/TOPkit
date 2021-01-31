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
        self._variables = []
        self._steps = []

    def add_variables(self, variables):
        for var in variables:
            self._variables.append(var)

    def reset_variables(self):
        self._variables = []

    def add_steps(self, steps):
        for step in steps:
            self._steps.append(step)

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


class nvpair:
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

    def add_header(self, header=" ", auth=FALSE, auth_user, auth_apppw):
        if auth == TRUE:
            auth_header = {"name": "Authorization",
                            "Value": 'Basic  ${_base64(_variables.'+auth_user.name+' + \":\" + _variables.'+auth_apppw.value+')}'
                            }
            self._headers.append(auth_header)
        else:
            self._headers.append(header)

    def link_body(self):
        pass

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
        self.is_nested = FALSE

    def update(self, name, value):
        self.name = name
        self.value = value

    def nest(self, name, n_name, n_value):
        self._nested_name = name
        self._nested_value = value
        self.is_nested = TRUE
        self.value = None

    def __repr__(self):
        if self.is_nested == FALSE:
            return {self.name:{
                                self.self._nested_name:self._nested_value
                                }
                    }
        else:
            return {self.name:self.value}

create-inc = actionsequence()
'''
"body": "{  \n\t\"status\": \"firstLine\",
            ---------------------------------------
            \n\t\"callerLookup\": {
            \n\t\t\"email\": \"${aanmelderemail}\"
            \n\t}
            \n}"

print("{\n\t\"status\": \"firstLine\",\n\t\"callerLookup\": {\n\t\t\"email\": \"${aanmelderemail}\"\n\t}\n}")
creates:
{
        "status": "firstLine",
        "callerLookup": {
                "email": "${aanmelderemail}"
        }
}
'''
