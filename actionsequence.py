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

    def add_variables(self, *args):
        for var in args:
            self._variables.append(var.build())

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

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def is_auth(self, user, pw):
        self.name = "Authorization"
        self.value = 'Basic  ${_base64(_variables.' \
                     + user.name + ' + \":\" + _variables.' \
                     + pw.name + ')}'

    # Function that updates variable
    def update(self, name, value):
        self.name = name
        self.value = value

    def build(self, auth=False, auth_user=None, auth_apppw=None):
        return {"name": self.name, "value": self.value}
        if auth is True:
            return {"name": "Authorization",
                    "value": 'Basic  ${_base64(_variables.'
                    + auth_user.name + ' + \":\" + _variables.'
                    + auth_apppw.name + ')}'}
        else:
            return {"name": self.name, "value": self.value}


class step():
    def __init__(self, name, method, url, escape, condition):
        self.name = name
        self.method = method
        self.url = url
        self.escape = escape
        self.condition = condition
        self._parameters = {}
        self._headers = []

    def add_headers(self, *args):
        for header in args:
            self._headers.append(header.build())

    def add_parameters(self, *args):
        for param in args:
            self._parameters.update(param.build())

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
