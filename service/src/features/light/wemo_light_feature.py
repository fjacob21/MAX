from wemo_env import wemo

class wemo_light_feature(object):

    def __init__(self, device):
        self._device = device
        self._wemo_device = wemo.get_device(self._device.ip)

    @property
    def name(self):
        return 'light'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Wemo Light control feature"

    def execute(self, cmd, params):
        if cmd == 'on':
            return self.on(params)
        elif cmd == 'off':
            return self.off(params)

    def on(self, params):
        self._wemo_device.on()
        return {'result': True}

    def off(self, params):
        self._wemo_device.off()
        return {'result': True}
