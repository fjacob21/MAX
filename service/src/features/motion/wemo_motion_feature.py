from wemo_env import wemo
import MAX

class wemo_motion_feature(object):

    def __init__(self, device):
        self._device = device
        self._wemo_device = wemo.get_device(self._device.name)
        self._current_state = self._wemo_device.get_state()
        wemo.register(self._device.name, self.motion)

    @property
    def name(self):
        return 'motion'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Wemo motion sensor feature"

    def execute(self, cmd, params):
        if cmd == 'state':
            return self.state(params)

    def state(self, params):
        return {'result': True, 'state': self._wemo_device.get_state()}

    def motion(self, state):
        if self._current_state != state:
            print('Fire event {st}!!!!!!!'.format(st=state))
            if state == 1:
                MAX.events.send_event('motionon', {})
            else:
                MAX.events.send_event('motionoff', {})
        self._current_state = state
