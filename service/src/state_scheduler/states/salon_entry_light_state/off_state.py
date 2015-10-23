import MAX
import time

class off_state(object):
    def __init__(self, machine):
        self._machine = machine
        self._lasttime = time.time()

    def event(self, event, source, params):
        if source.name == 'WeMo Motion':
            if event == 'motion_on' and self._machine.isLightNeeded():
                self._machine.set_state(self._machine._on_state)
        elif event == 'salon_entry_bt':
            self._machine.set_state(self._machine._prio_on_state)

    def enter(self):
        self._lasttime = time.time()
        print('Close salon light')
        MAX.devices.devices['WeMo Switch'].execute_feature('light', 1, 'off', {})
