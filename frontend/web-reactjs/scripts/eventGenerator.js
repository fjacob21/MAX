function eventGenerator(){
    newobj = {

    scripts:[],

    ctr: function(){

    },

    sendEvent: function(eventName, params){
      $.ajax({
        url: "/MAX/api/v1.0/event/",
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({"event":eventName}),
        success: function(data) {
        }.bind(this),
        error: function(xhr, status, err) {
          console.error("Error on execute ", status, err.toString());
        }.bind(this)
      });
    },
  }
  newobj.ctr();
  return newobj;
}
