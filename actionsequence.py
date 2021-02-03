import json


class actionsequence():
    '''Creates action sequence class. Bundles everything'''

    def __init__(self,
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
        '''Returns python DICT'''
        return {  # level 1
                "formatVersion": self.formatversion,
                "exportDate": self.exportdate,
                "actionSequence": {  # level 2
                    "name": self.name,
                    "description": "By MerijnA's TOPkit\n"+self.description,
                    "structureName": self.structurename,
                    "configuration": {
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

    # Function that updates variable
    def update(self, name, value):
        self.name = name
        self.value = value

    # Spit out variable in json style with necessary checks
    def json_build(self):
        return '{\n\t"name": "'+self.name+'",\n\t"value": "'+self.value+'"\n}'


class step():
    def __init__(self, name, method, url, escape, condition):
        self.name = name
        self.method = method
        self.url = url
        self.escape = escape
        self.condition = condition
        self._parameters = {}
        self._headers = []

    def add_header(self, header=" ",
                   auth=False, auth_user=None, auth_apppw=None):
        if auth is True:
            auth_header = {"name": "Authorization",
                           "value": 'Basic  ${_base64(_variables.'
                           + auth_user.name + ' + \":\" + _variables.'
                           + auth_apppw.name + ')}'}
            self._headers.append(auth_header)
        else:
            self._headers.append(header)

    def add_parameter(self, parameter):
        self._parameters.update(parameter)

    def build(self):
        return {
            "name": self.name,
            "method": self.method,
            "url": self.url,
            "headers": self._headers,
            "escapeBodyValues": self.escape,
            "body": repr(self._parameters),
            "executionCondition": self.condition,
            "customExecutionCondition": ""
            }


class parameter:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.is_nested = False

    def update(self, name, value):
        self.name = name
        self.value = value

    def nest(self, name, value):
        self._nested_name = name
        self._nested_value = value
        self.is_nested = True
        self.value = None

    def build(self):
        if self.is_nested is True:
            return {self.name: {
                                self._nested_name: self._nested_value
                                }
                    }
        else:
            return {self.name: self.value}


incidentcreator = actionsequence(formatversion="2.6", exportdate=1568803440466,
                                 name="Create an incident (Registered Caller)",
                                 description="Amazing story",
                                 structurename="incident1")

td_usr = nvpair(name="topdesk_user",
                value="Enter the name of your API Operator account")
td_pw = nvpair(name="topdesk_applicationpassword",
               value="Enter the application password")
td_url = nvpair(name="topdesk_url",
                value="Enter your TOPdesk URL here")

step1 = step(name="step1", method="POST",
             url="${_variables.topdesk_url?no_esc}/tas/api/incidents",
             escape=True, condition="ONLY_WHEN_PREVIOUS_SUCCEEDED")

h_type = nvpair(name="Content-Type", value="application/json")

p_status = parameter(name="status", value="firstLine")
p_caller = parameter(name="callerLookup")
p_caller.nest(name="email", value="${aanmelderemail}")

step1.add_header(h_type.build())
step1.add_header(auth=True, auth_user=td_usr, auth_apppw=td_pw)
step1.add_parameter(p_status.build())
step1.add_parameter(p_caller.build())
incidentcreator.add_variables(td_usr.build())
incidentcreator.add_variables(td_pw.build())
incidentcreator.add_variables(td_url.build())

incidentcreator.add_steps(step1.build())
print(json.dumps(incidentcreator.build(), indent=2))
