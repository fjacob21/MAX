import MAX
import time

class prio_off_state(object):
    def __init__(self, machine):
        self._machine = machine
        self._lasttime = time.time()

    def event(self, event, source, params):
        if event == 'bedroom_desk_bt':
            self._machine.set_state(self._machine._prio_on_state)

    def enter(self):
        self._lasttime = time.time()
        print('Close bedroom light in priority')
        MAX.devices.devices['WeMo Insight'].execute_feature('light', 1, 'off', {})
