#sudo pip install pyping
import pyping
import sys
import time

class device(object):
    def __init__(self, name, mac = '', ip = '', desc = '', img = ''):
        self._name = name
        self._desc = desc
        self._img = img
        self._mac = mac
        self._ip = ip
        self._features = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, val):
        self._mac = val

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, val):
        self._ip = val

    @property
    def description(self):
        return self._desc

    @description.setter
    def description(self, val):
        self._desc = val

    @property
    def image(self):
        return self._img

    @image.setter
    def image(self, val):
        self._img = val

    @property
    def features(self):
        return list(self._features.values())

    @property
    def json(self):
        obj = {}
        obj['name'] = self._name
        obj['mac'] = self._mac
        obj['ip'] = self._ip
        obj['desc'] = self._desc
        obj['img'] = self._img
        return obj

    def add_feature(self, feature):
        if (feature.name.lower(), feature.version) in self._features:
            return False

        self._features[(feature.name.lower(), feature.version)] = feature
        return True

    def del_feature(self, feature, version):
        if (feature,version) not in self._features:
            return False
        self._features.remove((feature,version))
        return True

    def is_online(self, params=None):
        try:
            r = pyping.Ping(self.ip)
            r.do()
            if r.receive_count == 1:
                isonline = True
            else:
                isonline = False
        except:
            print(sys.exc_info())
            isonline = False

        return {'result': True, 'isonline': isonline}

    def wait_online(self, params=None):
        wait_time = 0.01
        wait_retry = 100
        if 'wait_time' in params: wait_time = params['wait_time']
        if 'wait_retry' in params: wait_retry = params['wait_retry']

        for i in range(0,10000):
            if self.is_online(params)['isonline']:
                print(self.is_online(params))
                return {'result': True, 'isonline': True, 'wait_time': wait_time, 'wait_retry':wait_retry}
            time.sleep(0.01)
        return {'result': True, 'isonline': False, 'wait_time': wait_time, 'wait_retry':wait_retry}

    def execute_feature(self, feature, version, cmd, params=None):
        if (feature,version) in self._features:
            return self._features[(feature,version)].execute(cmd, params)
        return {'result': False, 'feature': feature, 'version': version, 'cmd':cmd, 'params':params}

    def execute(self, cmd, params=None):
        if cmd == 'online':
            return self.is_online(params)
        elif cmd == 'waitonline':
            return self.wait_online(params)
        return {'result': False}
