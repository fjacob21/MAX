import MAX
import time
from .prio_off_state import prio_off_state
from .prio_on_state import prio_on_state

class bedroom_desk_light_state(object):
    def __init__(self):
        self._prio_off_state = prio_off_state(self)
        self._prio_on_state = prio_on_state(self)
        self.set_state(self._prio_off_state)

    @property
    def name(self):
        return 'Salont entry light state'

    @property
    def description(self):
        return "State machine that control the salon entry light"

    def isMorning(self):
        now = time.localtime()
        return now.tm_hour >= 6 and now.tm_hour <= 7

    def isEvening(self):
        now = time.localtime()
        return now.tm_hour >= 18 and (now.tm_hour <= 21 and now.tm_min <= 55)

    def isLightNeeded(self):
        return self.isMorning() or self.isEvening()

    def set_state(self, state):
        self._current_state = state
        self._current_state.enter()

    def event(self, event, source, params):
        #Sprint('Fire {device}.{event}'.format(event=event, device=source.name))
        self._current_state.event(event, source, params)
