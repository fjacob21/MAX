function device(deviceId){
    newobj = {

    firstUpdate: true,
    id:deviceId,

    ctr: function(){
            this.refreshData();
    },

    addFeatureFunctions: function(){
        firstUpdate = false;
        for(i=0;i<this.device.features.length;i++) {
                console.log(this.device.features[i].name)
                this[this.device.features[i].name] = {}
                this[this.device.features[i].name].device = this.device;
                this[this.device.features[i].name].name = this.device.features[i].name;
                this[this.device.features[i].name].version = this.device.features[i].version;
                for(j=0;j<this.device.features[i].functions.length;j++){
                        var fobj = {
                                "device": this,
                                "feature":this.device.features[i].name,
                                "fct":this.device.features[i].functions[j],
                                "version":this.device.features[i].version
                        };
                        this[this.device.features[i].name][this.device.features[i].functions[j]] = function(params, success, error)
                        {
                                this.device.executeFeature(this.feature,
                                        this.fct,
                                        this.version,
                                        params, success, error
                                );
                        }.bind(fobj);
                }
        }
    },
    build_request_url: function(request){
      return "/MAX/api/v1.0/" + request + "/";
    },
    executeFeature: function(feature, cmd, version, params, success, error){
      $.ajax({
        url: this.build_request_url('devices/' + this.id + '/' + feature + '/' + version + '/' + cmd),
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(params),
        success: success,
        error: error
      });
    },

    refreshData: function(){
      $.ajax({
        url: this.build_request_url("devices/" + this.id),
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.device = data.device;
          if(this.firstUpdate)
                this.addFeatureFunctions()
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
