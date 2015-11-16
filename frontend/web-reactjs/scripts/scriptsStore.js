function scriptsStore(){
    newobj = {

    scripts:[],

    ctr: function(){
      this.refreshData();
      //setInterval(this.refreshData.bind(this), 2000);
    },

    build_request_url: function(request){
      return "/MAX/api/v1.0/" + request + "/";
    },

    getScripts: function(){
      return this.devices;
    },

    execute: function(script, version){
      $.ajax({
        url: this.build_request_url('scripts/' + script + '/' + version),
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({}),
        success: function(data) {
          //this.devices = data.devices;
          alert('Script executed!');
        }.bind(this),
        error: function(xhr, status, err) {
          alert("Error on execute ", status, err.toString());
        }.bind(this)
      });
    },

    refreshData: function(){
      $.ajax({
        url: this.build_request_url("scripts"),
        dataType: 'json',
        cache: false,
        success: function(data) {
          this.scripts = data.scripts;
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on scripts refresh", status, err.toString());
        }.bind(this)
      });
    },
  }
  newobj.ctr();
  return newobj;
}
