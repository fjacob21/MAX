
class script(object):

    def __init__(self, name, version, desc, script_class):
        self._name = name
        self._version = version
        self._desc = desc
        self._script_class = script_class

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def description(self):
        return self._desc

    @property
    def script_class(self):
        return self._script_class

    @property
    def json(self):
        obj = {}
        obj['name'] = self._name
        obj['version'] = self._version
        obj['desc'] = self._desc
        return obj
