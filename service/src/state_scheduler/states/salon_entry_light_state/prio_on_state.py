import MAX
import time

class prio_on_state(object):
    def __init__(self, machine):
        self._machine = machine
        self._lasttime = time.time()

    def event(self, event, source, params):
        if event == 'salon_entry_bt':
            self._machine.set_state(self._machine._prio_off_state)

    def enter(self):
        self._lasttime = time.time()
        print('Open salon light in priority')
        MAX.devices.devices['WeMo Switch'].execute_feature('light', 1, 'on', {})
