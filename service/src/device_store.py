from device import device

class device_store(object):

    def __init__(self):
        self._devices = {}

    def add_device(self, device_json):
        if device_json['name'] in self._devices:
            return False

        deviceobj = device(device_json['name'])
        self._devices[device_json['name']] = deviceobj
        self.update_device(deviceobj.name, device_json)

        return True

    def update_device(self, name, device_json):
        if name not in self._devices:
            return False
        deviceobj = self._devices[name]
        if 'name' in device_json and device_json['name'] != deviceobj.name:
            del self._devices[name]
            deviceobj.name = device_json['name']
            self._devices[device_json['name']] = deviceobj
        if 'ip' in device_json: deviceobj.ip = device_json['ip']
        if 'mac' in device_json: deviceobj.mac = device_json['mac']
        if 'desc' in device_json: deviceobj.description = device_json['desc']
        if 'img' in device_json: deviceobj.image = device_json['img']

        return True

    def del_device(self, device):
        if device not in self._devices:
            return False
        del self._devices[device]
        return True

    @property
    def devices(self):
        return self._devices
