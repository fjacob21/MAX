#sudo pip install pyping
import pyping
import sys

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
        if feature.name in self._features:
            return False

        self._features[feature.name] = feature
        return True

    def del_feature(self, feature):
        if feature not in self._features:
            return False
        self._features.remove(feature)
        return True

    def is_online(self, params):
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

    def wait_online(self, params):
        return {'result': True, 'isonline': True}

    def execute_feature(self, feature, cmd, params):
        if feature == 'tv':
            import tv_feature
            tv = tv_feature.tv_feature(self)
            tv.execute(cmd, params)
        return {'result': True, 'feature': feature, 'cmd':cmd, 'params':params}

    def execute(self, cmd, params):
        cmd_part = cmd.split('.')
        if len(cmd_part) == 1:
            if cmd == 'online':
                return self.is_online(params)
            elif cmd == 'waitonline':
                return self.wait_online(params)
        else:
            return self.execute_feature(cmd_part[0], cmd_part[1], params)
        return {'result': True}
