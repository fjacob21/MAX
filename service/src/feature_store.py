import os
import sys

from feature import feature

class feature_store(object):

    def __init__(self):
        self._features = {}

    def register(self, name, version, desc, feature_class):
        if (name.lower(),version) in self._features:
            print('Feature already present!')
            return False

        self._features[(name.lower(), version)] = feature(name, version, desc, feature_class)
        return True

    def load_features(self):
        sys.path.append('./features')
        for feature in os.listdir('./features'):
            __import__(feature)

    def get_feature_class(self, name, version):
        if (name.lower(),version) not in self._features:
            return None
        return self._features[(name.lower(), version)].feature_class

    @property
    def features(self):
        return self._features
