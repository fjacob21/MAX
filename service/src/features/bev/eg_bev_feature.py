from eg_networksender import Send

class eg_bev_feature(object):

    def __init__(self, device):
        self._device = device

    @property
    def name(self):
        return 'bev'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Control Bell ExpressVu using evenghost receiver"

    def execute(self, cmd, params):
        if cmd == 'enter':
            return self.enter(params)

    def enter(self, params):
        return {'result': Send('EnterBEV', self._device.ip)}
