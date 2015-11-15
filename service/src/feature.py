class feature(object):

    def __init__(self, name, version, desc, feature_class):
        self._name = name
        self._version = version
        self._desc = desc
        self._feature_class = feature_class

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
    def feature_class(self):
        return self._feature_class

    @property
    def json(self):
        print('json', self)
        obj = {}
        obj['name'] = self._name
        obj['version'] = self._version
        obj['description'] = self._desc
        return obj
