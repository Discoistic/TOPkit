import json
class actionsequence():
    def __init__(   self,
                    formatversion="2.6",
                    exportdate=832217040,
                    name=" -- ",
                    description=" -- ",
                    structurename=" -- "):
        self.formatversion = formatversion
        self.exportdate = exportdate
        self.name = name
        self.description = description
        self.structurename = structurename
        self._variables = []
        self._steps = []

    def add_variables(self, variable):
        self._variables.append(variable)

    def reset_variables(self):
        self._variables = []

    def add_steps(self, step):
        self._steps.append(step)

    def reset_steps(self, step):
        self._steps = []


    def build(self):
        return { # level 1
        "formatversion": self.formatversion,
        "exportDate": self.exportdate,
        "actionSequence":{ # level 2
            "name": self.name,
            "description": "AUTO-GENERATED by MerijnA's TOPkit\n "+self.description,
            "structureName": self.structurename,
            "configuration":{
                "variables": self._variables,
                "mappingDefinitions": [],
                "steps": self._steps
                }
            }
        }


class nvpair:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def build(self):
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
        self.escape = escape
        self.condition = condition
        self._headers = []

    def add_header(self, header=" ", auth=False, auth_user=None, auth_apppw=None):
        if auth is True:
            auth_header = {"name": "Authorization",
                            "Value": 'Basic  ${_base64(_variables.'+auth_user.name+' + \":\" + _variables.'+auth_apppw.name+')}'
                            }
            self._headers.append(auth_header)
        else:
            self._headers.append(header)

    def add_to_body(self):
        pass

    def build(self):
        return {
            "name": self.name,
            "method": self.method,
            "url": self.url,
            "headers": self._headers,
            "escapeBodyValues": self.escape,
            "body":  " ",  # FILL
            "executionCondition": self.condition,
            "customExecutionCondition": ""
            }

class parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.is_nested = False

    def update(self, name, value):
        self.name = name
        self.value = value

    def nest(self, name, name, value):
        self._nested_name = name
        self._nested_value = value
        self.is_nested = TRUE
        self.value = None

    def build(self):
        if self.is_nested is False:
            return {self.name:{
                                self.self._nested_name:self._nested_value
                                }
                    }
        else:
            return {self.name:self.value}

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
incidentcreator = actionsequence(formatversion="2.6", exportdate=1568803440466,
                                 name="Create an incident (Registered Caller)",
                                 description="KI 11169\nVersion: 1.1\nDate: 18-09-2019\nAuthor: ChrisF / ChloEM\n\nStep 1: Create a new 1st line incident as a registered caller according to the details specified in the body of the step.\n\nTo add more fields in the body, please see:\n\nhttps://developers.topdesk.com/documentation/index.html#api-Incident-CreateIncident",
                                 structurename="incident1")

td_usr = nvpair(name="topdesk_user", value="Enter the name of your API Operator account")
td_pw = nvpair(name="topdesk_applicationpassword", value="Enter the application password")
td_url = nvpair(name="topdesk_url", value="Enter your TOPdesk URL here")

step1 = step(name="step1", method="POST", url="${_variables.topdesk_url?no_esc}/tas/api/incidents", escape=True, condition="ONLY_WHEN_PREVIOUS_SUCCEEDED")

h_type = nvpair(name="Content-Type", value="application/json")
step1.add_header(h_type.build())
step1.add_header(auth=True, auth_user=td_usr, auth_apppw=td_pw)



incidentcreator.add_variables(td_usr.build())
incidentcreator.add_variables(td_pw.build())
incidentcreator.add_variables(td_url.build())

incidentcreator.add_steps(step1.build())

print(json.dumps(incidentcreator.build()))
