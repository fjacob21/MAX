# File for managing the MAX system
from device_store import device_store
from feature_store import feature_store
from script_store import script_store
import imp
import os
import sys

print('Initializing MAX Power...')

#max = imp.new_module('MAX')
#print(max)
#sys.modules['MAX'] = max
#We really need to keep this order of loading stores!!!

features = feature_store()
features.load_features()
devices = device_store(features)
devices.load_devices()
scripts = script_store(devices)
scripts.load_scripts()
