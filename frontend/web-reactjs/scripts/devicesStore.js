function devicesStore(){
    newobj = {

    devices:[],
    updateListeners:[],

    ctr: function(){
      this.refreshData();
      setInterval(this.refreshData.bind(this), 2000);
    },

    build_request_url: function(request){
      return "/MAX/api/v1.0/" + request + "/";
    },
    execute_feature: function(device, feature, cmd, version){
      $.ajax({
        url: this.build_request_url('devices/' + device + '/' + feature + '/' + cmd + '/' + version),
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({}),
        success: function(data) {
          //this.devices = data.devices;
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on execute ", status, err.toString());
        }.bind(this)
      });
    },
    addDevice: function(device){
      $.ajax({
        url: this.build_request_url("devices"),
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(device),
        success: function(data) {
          this.devices = data.devices;
          this.emit();
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on add device ", status, err.toString());
        }.bind(this)
      });
    },

    updateDevice: function(name, device){
      $.ajax({
        url: this.build_request_url("devices/" + name),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        type: 'PUT',
        data: JSON.stringify(device),
        success: function(data) {
          this.devices = data.devices;
          this.emit();
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on update device ", status, err.toString());
        }.bind(this)
      });
    },

    deleteDevice: function(device){
      $.ajax({
        url: this.build_request_url("devices/" + device.name),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        type: 'DELETE',
        data: JSON.stringify(device),
        success: function(data) {
          this.devices = data.devices;
          this.emit();
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on update device ", status, err.toString());
        }.bind(this)
      });
    },

    getDevices: function(){
      return this.devices;
    },

    emit: function(){
        for(i=0;i<this.updateListeners.length;i++)
          this.updateListeners[i]();
    },

    addListener: function(listener){
      this.updateListeners.push(listener);
    },

    deleteListener: function(listener){
      idx = this.updateListeners.indexOf(listener)
      if(idx != -1)
        this.updateListeners.splice(idx);
    },

    refreshData: function(){
      $.ajax({
        url: this.build_request_url("devices"),
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.devices = data.devices;
          this.emit();
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on refresh", status, err.toString());
        }.bind(this)
      });
    },
  }
  newobj.ctr();
  return newobj;
}
