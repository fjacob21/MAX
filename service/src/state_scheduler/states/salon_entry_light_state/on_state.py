import MAX
import time

class on_state(object):
    def __init__(self, machine):
        self._machine = machine
        self._lasttime = time.time()

    def event(self, event, source, params):
        if source.name == 'WeMo Motion':
            dt = (time.time() - self._lasttime) / 60
            if event == 'motion_off' and dt > 15:
                self._machine.set_state(self._machine._off_state)
            if event == 'motion_on' and self._machine.isLightNeeded():
                self._lasttime = time.time()
        elif event == 'salon_entry_bt':
            self._machine.set_state(self._machine._prio_off_state)

    def enter(self):
        self._lasttime = time.time()
        print('Open salon light')
        MAX.devices.devices['Salonlightdoor'].execute_feature('light', 1, 'on', {})
