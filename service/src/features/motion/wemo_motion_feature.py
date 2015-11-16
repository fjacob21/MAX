from wemo_env import wemo
import MAX

class wemo_motion_feature(object):

    def __init__(self, device):
        self._device = device
        self._wemo_device = wemo.get_device(self._device.ip)
        self._current_state = self._wemo_device.get_state()
        wemo.register(self._device.ip, self.motion)

    @property
    def name(self):
        return 'motion'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Wemo motion sensor feature"

    @property
    def functions(self):
        return ['state']

    def execute(self, cmd, params):
        if cmd == 'state':
            return self.state(params)

    def state(self, params):
        return {'device':self._device.json, 'feature':self.name, 'result': True, 'state': self._wemo_device.get_state()}

    def motion(self, state):
        #if self._current_state != state:
        if state == 1:
            MAX.events.event('motion_on', self._device, {})
        else:
            MAX.events.event('motion_off', self._device, {})
        self._current_state = state
