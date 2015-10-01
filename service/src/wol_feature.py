#pip install wakeonlan

from wakeonlan import wol

class wol_feature(object):

    def __init__(self, device):
        self._device = device

    @property
    def name(self):
        return 'wol'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Wake On Lan feature"

    def execute(self, cmd, params):
        if cmd == 'wake':
            return wake(params)

    def wake(self, params):
        #wol.send_magic_packet('F8:0F:41:2B:84:94')
        wol.send_magic_packet(self._device.mac)
        return {'result': True}
