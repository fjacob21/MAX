
class closehouse_script(object):

    def __init__(self, device_store):
        self._devices = device_store

    @property
    def name(self):
        return 'closehouse'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Script to close my house things"

    def execute(self, params):
        print('Close my house :)')
        salon = self._devices.devices['Salon']
        if salon.is_online()['isonline']:
            if not salon.execute_feature('tv', 1, 'close')['result']:
                return {'result': False}

        return {'result': True}
