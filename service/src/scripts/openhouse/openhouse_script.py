
class openhouse_script(object):

    def __init__(self, device_store):
        self._devices = device_store

    @property
    def name(self):
        return 'openhouse'

    @property
    def version(self):
        return 1

    @property
    def description(self):
        return "Script to open my house things"

    def execute(self, params):
        print('Open my house :)')
        salon = self._devices.devices['Salon']
        if not salon.is_online()['isonline']:
            print('TV not open, so wake it...')
            if not salon.execute_feature('wol', 1, 'wake')['result']:
                return {'result': False}
            if not salon.wait_online({'wait_time':1, 'wait_retry': 20})['isonline']:
                return {'result': False}

        if not salon.execute_feature('tv', 1, 'open')['result']:
            return {'result': False}
        return {'result': True}
