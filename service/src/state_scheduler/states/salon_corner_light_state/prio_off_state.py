import MAX
import time

class prio_off_state(object):
    def __init__(self, machine):
        self._machine = machine
        self._lasttime = time.time()

    def event(self, event, source, params):
        if source.name == 'Salonlightcorner':
            if event == 'light_on':
                print('light_on')
                self._machine.set_state(self._machine._prio_on_state)
        if event == 'salon_corner_bt':
            self._machine.set_state(self._machine._prio_on_state)

    def enter(self):
        self._lasttime = time.time()
        print('Close salon corner light in priority')
        MAX.devices.devices['Salonlightcorner'].execute_feature('light', 1, 'off', {})
