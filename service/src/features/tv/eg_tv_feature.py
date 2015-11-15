from eg_networksender import Send

class eg_tv_feature(object):

    def __init__(self, device):
        self._device = device

    @property
    def name(self):
        return 'tv'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Control TV using evenghost receiver"

    @property
    def functions(self):
        return ['open', 'close', 'state']

    def execute(self, cmd, params):
        if cmd == 'open':
            return self.open(params)
        if cmd == 'close':
            return self.close(params)
        if cmd == 'state':
            return self.state(params)

    def open(self, params):
        return {'device':self._device.json, 'feature':self.name, 'result': Send('OpenTV', self._device.ip)}

    def close(self, params):
        return {'device':self._device.json, 'feature':self.name, 'result': Send('CloseTV', self._device.ip)}

    def state(self, params):
        if self._device.is_online()['isonline'] == False:
            return {'device':self._device.json, 'feature':self.name, 'result': True, 'state': 0}
        result = Send('GetState', self._device.ip)
        return {'device':self._device.json, 'feature':self.name, 'result': Send('GetState', self._device.ip)}
