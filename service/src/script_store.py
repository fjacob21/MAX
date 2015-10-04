import os
import sys

from script import script

class script_store(object):

    def __init__(self, device_store):
        self._scripts = {}
        self._devices = device_store

    def register(self, name, version, desc, script_class):
        if (name.lower(),version) in self._scripts:
            print('Script already present!')
            return False

        self._scripts[(name.lower(), version)] = script(name, version, desc, script_class)
        return True

    def load_scripts(self):
        sys.path.append('./scripts')
        for script in os.listdir('./scripts'):
            __import__(script)

    def get_script_class(self, name, version):
        if (name.lower(),version) not in self._scripts:
            return None
        return self._scripts[(name.lower(), version)].script_class

    @property
    def scripts(self):
        return self._scripts

    def execute_script(self, name, version, params=None):
        if (name.lower(),version) not in self._scripts:
            return {'result': False}

        script_class = self.get_script_class(name, version)
        script = script_class(self._devices)
        return script.execute(params)
