#!flask/bin/python
from flask import Flask, jsonify, abort, request, send_from_directory, redirect, url_for
import json
import MAX

app = Flask(__name__, static_url_path='')
store = MAX.devices
scripts = MAX.scripts

# Devices Section ====================================================
@app.route('/MAX/api/v1.0/devices/', methods=['GET'])
def get_devices():
    devices = []
    for key, value in store.devices.iteritems():
        devices.append(value.json)

    return jsonify({"devices": devices})

@app.route('/MAX/api/v1.0/devices/<string:device>/', methods=['GET'])
def get_device(device):
    if device not in store.devices:
        abort(404)
    return jsonify({"device": store.devices[device].json})

@app.route('/MAX/api/v1.0/devices/', methods=['POST'])
def add_device():
    device = request.get_json()
    print('received:', device)
    if device is None or 'name' not in device:
        abort(400)

    if not store.add_device(device):
        return abort(400)
    return get_devices()

@app.route('/MAX/api/v1.0/devices/<string:device>/', methods=['PUT'])
def update_device(device):
    if device not in store.devices:
        abort(404)

    device_json = request.get_json()
    if device_json is None:
        abort(400)

    #Update device
    store.update_device(device, device_json)
    return get_devices()

@app.route('/MAX/api/v1.0/devices/<string:device>/', methods=['DELETE'])
def delete_device(device):
    if device not in store.devices:
        abort(404)

    if store.del_device(device) == False:
        return abort(404)

    return get_devices()

@app.route('/MAX/api/v1.0/devices/<string:device>/<string:cmd>/', methods=['POST'])
def execute_cmd(device, cmd):
    if device not in store.devices:
        abort(404)

    param_json = request.get_json()

    #Execute cmd
    return jsonify(store.devices[device].execute(cmd, param_json))

@app.route('/MAX/api/v1.0/devices/<string:device>/<string:feature>/<int:version>/<string:cmd>/', methods=['POST'])
def execute_feature_cmd(device, feature, version, cmd):
    if device not in store.devices:
        abort(404)

    param_json = request.get_json()

    #Execute cmd
    return jsonify(store.devices[device].execute_feature(feature, version, cmd, param_json))

# Scripts Section ====================================================
@app.route('/MAX/api/v1.0/scripts/', methods=['GET'])
def get_scripts():
    scripts_json = []
    for key, value in scripts.scripts.iteritems():
        scripts_json.append(value.json)

    return jsonify({"scripts": scripts_json})

@app.route('/MAX/api/v1.0/scripts/<string:script>/<int:version>/', methods=['POST'])
def execute_script(script, version):
    #if script not in scripts.scripts:
    #    abort(404)

    param_json = request.get_json()

    #Execute script
    return jsonify(scripts.execute_script(script, version, param_json))

# Static WEB section ============================================
@app.route('/html/<path:path>')
def send_js(path):
    return send_from_directory('../../frontend/web-reactjs', path)

@app.route('/')
def root():
    return redirect('/html/index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
