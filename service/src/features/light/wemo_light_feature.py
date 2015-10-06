#pip install ouimeaux

from ouimeaux.environment import Environment

class wemo_light_feature(object):

    def __init__(self, device):
        self._device = device
        self._wemo_env = Environment(with_discovery=False, with_subscribers=False)
        self._wemo_env.start()
        self._wemo_device = self._wemo_env.get(self._device.name)

    #def __del__(self):
    #    print('delete wemo')
    #    del(self._wemo_env)

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
