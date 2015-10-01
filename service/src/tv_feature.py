from eg_networksender import Send

class tv_feature(object):

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

    def execute(self, cmd, params):
        if cmd == 'open':
            return self.open(params)
        if cmd == 'close':
            return self.close(params)

    def open(self, params):
        return {'result': Send('OpenTV', self._device.ip)}

    def close(self, params):
        return {'result': Send('CloseTV', self._device.ip)}
