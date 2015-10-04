from device import device
import json

class device_store(object):

    def __init__(self, features):
        self._devices = {}
        self._features = features

    def load_devices(self, file='../db/devices.json'):
        with open(file) as data:
            devices=json.load(data)

        for device in devices['devices']:
            self.add_device(device)

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
        if 'features' in device_json:
            for feature_json in device_json['features']:
                feature_class = self._features.get_feature_class(feature_json['name'], int(feature_json['version']))
                if feature_class is not None:
                    feature = feature_class(deviceobj)
                    deviceobj.add_feature(feature)

        return True

    def del_device(self, device):
        if device not in self._devices:
            return False
        del self._devices[device]
        return True

    @property
    def devices(self):
        return self._devices
