import MAX
import time
from .off_state import off_state
from .on_state import on_state
from .prio_off_state import prio_off_state
from .prio_on_state import prio_on_state

class salon_entry_light_state(object):
    def __init__(self):
        self._off_state = off_state(self)
        self._on_state = on_state(self)
        self._prio_off_state = prio_off_state(self)
        self._prio_on_state = prio_on_state(self)
        self.set_state(self._off_state)

    @property
    def name(self):
        return 'Salont entry light state'

    @property
    def description(self):
        return "State machine that control the salon entry light"

    def isMorning(self):
        now = time.localtime()
        isMorning = now.tm_hour >= 6 and now.tm_hour <= 8
        print("Is it morning? {0}".format(isMorning))
        return isMorning

    def isEvening(self):
        now = time.localtime()
        isEvening = now.tm_hour >= 18 and (now.tm_hour <= 21 and now.tm_min <= 55)
        print("Is it evening? {0}".format(isEvening))
        return isEvening

    def isLightNeeded(self):
        isLightNeeded = self.isMorning() or self.isEvening()
        print("Is light needed? {0}".format(isLightNeeded))
        return isLightNeeded

    def set_state(self, state):
        self._current_state = state
        self._current_state.enter()

    def event(self, event, source, params):
        #Sprint('Fire {device}.{event}'.format(event=event, device=source.name))
        self._current_state.event(event, source, params)