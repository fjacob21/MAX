from wemo_env import wemo
import MAX

class wemo_light_feature(object):

    def __init__(self, device):
        self._device = device
        self._wemo_device = wemo.get_device(self._device.ip)
        self._current_state = self._wemo_device.get_state()
        wemo.register(self._device.ip, self.change_event)

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

    def change_event(self, state):
        #print(self._device.name, state)
        if self._current_state != state:
            self._current_state = state
            #if state == 1:
                #print(self._device.name, 'send light_on')
                #MAX.events.event('light_on', self._device, {})
            #else:
                #print(self._device.name, 'send light_off')
                #MAX.events.event('light_off', self._device, {})

    def _get_state(self):
        state = self._wemo_device.get_state(True)
        if state != 0:
            state = 1
        return state

    def get_state(self, params):
        state = self._get_state()
        return {'device':self._device.json, 'feature':self.name, 'result': True, 'state':state}

    def on(self, params):
        if self._get_state() == 0:
            self._wemo_device.on()
        return {'device':self._device.json, 'feature':self.name, 'result': True}

    def off(self, params):
        if self._get_state() == 1:
            self._wemo_device.off()
        return {'device':self._device.json, 'feature':self.name, 'result': True}
