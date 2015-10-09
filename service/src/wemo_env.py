#pip install ouimeaux
from ouimeaux.environment import Environment
#from ouimeaux.utils import matcher
from ouimeaux.signals import receiver, statechange, devicefound
import thread
import time
#_env = Environment()
#_env.start()

class wemo_env(object):

    # @receiver(devicefound)
    # def found(sender, **kwargs):
    #     #if matches(sender.name):
    #         print "Found device:", sender.name
    #
    # @receiver(statechange)
    # def motion(sender, **kwargs):
    #     #if matches(sender.name):
    #         print "{} state is {state}".format(
    #             sender.name, state="on" if kwargs.get('state') else "off")

    def __init__(self):
        self._stop_flag = False
        self._thread = None
        self._env = Environment()
        #try:
        self._env.start()
        self._env.discover(10)
        #except:
        #    print "WeMo environment cannot start ;( !!!!"

    def get_device(self, name):
        return self._env.get(name)

    def start(self):
        self._stop_flag = False
        self._thread = thread.start_new_thread( self.wemo_thread, () )
        print('end start')

    def stop(self):
        self._stop_flag = True

    def wemo_thread(self):
        try:
            #self._env.discover(10)
            print('WeMo Thread starting')
            print(self._env)
            self._env.wait()
            print('End of wemo thread')
        except:
            print "WeMo environment is DEATH ;( !!!!"


#wemo.start()
@receiver(devicefound)
def found(sender, **kwargs):
    #if matches(sender.name):
        print "Found device:", sender.name

@receiver(statechange)
def motion(sender, **kwargs):
    #if matches(sender.name):
        print "{} state is {state}".format(
            sender.name, state="on" if kwargs.get('state') else "off")

wemo = wemo_env()
wemo.start()
#while 1:
#    pass
wemo._env.wait()

# @receiver(devicefound)
# def found(sender, **kwargs):
#     #if matches(sender.name):
#         print "Found device:", sender.name
#
# @receiver(statechange)
# def motion(sender, **kwargs):
#     #if matches(sender.name):
#         print "{} state is {state}".format(
#             sender.name, state="on" if kwargs.get('state') else "off")

# env = Environment()
# try:
#     env.start()
#     env.discover(10)
#     env.wait()
# except (KeyboardInterrupt, SystemExit):
#     print "Goodbye!"
#     sys.exit(0)
