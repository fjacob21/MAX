#pip install ouimeaux
import gevent
from ouimeaux.environment import Environment
from ouimeaux.signals import receiver, statechange, devicefound

class wemo_env(object):

    def __init__(self):
        self._watcheux = {}
        self._env = Environment()
        try:
            self._env.start()
            self._env.discover(3)
        except:
            print("WeMo environment cannot start ;( !!!!")

    def start_watching(self):
        statechange.connect(self.update_state,
                        unique=False,
                        dispatch_uid=id(self))

    def get_device(self, name):
        return self._env.get(name)

    def register(self, name, fct):
        if name not in self._watcheux:
            self._watcheux[name] = []
        self._watcheux[name].append(fct)
        if len(self._watcheux) > 0:
            self.start_watching()

    def update_state(self, sender, **kwargs):
        state = kwargs.get('state')
        if state != 0:
            state = 1
        if sender.name in self._watcheux:
            for watcheu in self._watcheux[sender.name]:
                watcheu(state)

        #print "{} state is {state}".format(
        #    sender.name, state="on" if kwargs.get('state') else "off")

wemo = wemo_env()
