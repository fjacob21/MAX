import os
import sys
import MAX

class state_event_scheduler(object):

    def __init__(self):
        self._states = []
        self.load_states()

    def event(self, event, source, params):
        for state in self._states:
            state.event(event, source, params)

    def load_states(self):
        sys.path.append('./state_scheduler/states')
        for state in os.listdir('./state_scheduler/states'):
            module = __import__(state)
            class_ = getattr(module, state)
            instance = class_()
            self._states.append(instance)
