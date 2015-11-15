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

    @property
    def functions(self):
        return ['on', 'off', 'state']

    def execute(self, cmd, params):
        if cmd == 'on':
            return self.on(params)
        elif cmd == 'off':
            return self.off(params)
        elif cmd == 'state':
            return self.get_state(params)

    def get_state(self, params):
        return {'device':self._device.json, 'feature':self.name, 'result': True, 'state':self._wemo_device.get_state()}

    def on(self, params):
        self._wemo_device.on()
        return {'device':self._device.json, 'feature':self.name, 'result': True}

    def off(self, params):
        self._wemo_device.off()
        return {'device':self._device.json, 'feature':self.name, 'result': True}
