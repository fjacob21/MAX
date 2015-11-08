var store = devicesStore();
var scripts = scriptsStore();

var HomeScreen = React.createClass({
  openHouse: function(){
    scripts.execute('openhouse', '1')
  },
  closeHouse: function(){
    scripts.execute('closehouse', '1')
  },
  openLight: function(){
    store.execute_feature('WeMo Insight', 'light', '1', 'on')
    store.execute_feature('WeMo Switch', 'light', '1', 'on')
  },
  closeLight: function(){
    store.execute_feature('WeMo Insight', 'light', '1', 'off')
    store.execute_feature('WeMo Switch', 'light', '1', 'off')
  },
  render: function() {
    return (
      <div className="homeScreen" >
        <button type="button" className="big-bt btn btn-default inline " onClick={this.openHouse}>Open house</button>
        <button type="button" className="btn btn-default inline big-bt" onClick={this.closeHouse}>Close house</button>
        <button type="button" className="btn btn-default inline big-bt" onClick={this.openLight}>Open lights</button>
        <button type="button" className="btn btn-default inline big-bt" onClick={this.closeLight}>Close lights</button>
      </div>
    );
  }
});

var DeviceBar = React.createClass({
  onAddDevice: function(){
    this.props.onAddDevice();
  },
  render: function() {
    return (
      <div className="deviceBar bar" >
        <h3 className="inline">Devices</h3>
        <button type="button" className="btn btn-default inline glyphicon glyphicon-plus" onClick={this.onAddDevice}/>
      </div>
    );
  }
});

var Device = React.createClass({
  getInitialState: function() {
    var device = this.props.device;
    if(!device){
      device = {
          name: "",
          mac: "",
          ip: "",
          desc: "",
        };
      }
    return {device: device};
  },
  handleChange: function(event) {
    var device = {
      name: React.findDOMNode(this.refs.name).value.trim(),
      mac: React.findDOMNode(this.refs.mac).value.trim(),
      ip: React.findDOMNode(this.refs.ip).value.trim(),
      desc: React.findDOMNode(this.refs.desc).value.trim(),
    };
    this.setState({device: device});
  },
  onCancel: function(){
    this.props.setDeviceList();
  },
  onClickDevice: function(){
    if(this.props.mode == 1){ //Add device
      device = {
        name: React.findDOMNode(this.refs.name).value.trim(),
        mac: React.findDOMNode(this.refs.mac).value.trim(),
        ip: React.findDOMNode(this.refs.ip).value.trim(),
        desc: React.findDOMNode(this.refs.desc).value.trim(),
      };
      store.addDevice(device);
    } else {//Update device
      device = {
        name: React.findDOMNode(this.refs.name).value.trim(),
        mac: React.findDOMNode(this.refs.mac).value.trim(),
        ip: React.findDOMNode(this.refs.ip).value.trim(),
        desc: React.findDOMNode(this.refs.desc).value.trim(),
      };
      store.updateDevice(this.props.name, device);
    }
    this.props.setDeviceList();
  },
  render: function() {
    var btLabel = "Add";
    if(this.props.mode == 2)
      btLabel = "Update";
    var device = this.state.device;
    return (
      <div className="device">
        <div><div className="device-label inline">Name</div> <input className="inline" type="text" ref="name" value={device.name} onChange={this.handleChange}/></div>
        <div><div className="device-label inline">MAC</div>  <input className="inline" type="text" ref="mac" value={device.mac} onChange={this.handleChange}/></div>
        <div><div className="device-label inline">ip</div>  <input className="inline" type="text" ref="ip" value={device.ip} onChange={this.handleChange}/></div>
        <div><div className="device-label inline">Description</div>  <input className="inline" type="text" ref="desc" value={device.desc} onChange={this.handleChange}/></div>
        <button type="button" className="btn btn-default" onClick={this.onClickDevice}>{btLabel}</button>
        <button type="button" className="btn btn-default" onClick={this.onCancel}>Cancel</button>
      </div>
    );
  }
});

var DeviceSummary = React.createClass({
  onEdit: function(device){
    this.props.setUpdateDevice(device);
  },
  onDelete: function(device){
    this.props.deleteDevice(device);
  },
  render: function() {
    return (
      <div className="deviceSummary">
        <div className="deviceName inline">
          {this.props.name}
        </div>
        <button type="button" className="btn btn-default inline" onClick={this.onEdit}>Edit</button>
        <button type="button" className="btn btn-default inline" onClick={this.onDelete}>Delete</button>
      </div>
    );
  }
});

var DeviceList = React.createClass({
  setUpdateDevice: function(device){
    this.props.setUpdateDevice(device);
  },
  deleteDevice: function(device){
    store.deleteDevice(device);
  },
  render: function() {
    var deviceNodes = this.props.devices.map(function (device) {
      return (
        <DeviceSummary key={device.name} name={device.name} deleteDevice={this.deleteDevice.bind(this, device)} setUpdateDevice={this.setUpdateDevice.bind(this, device)}/>
      );
    },this);
    return (
      <div className="deviceList">
        {deviceNodes}
      </div>
    );
  }
});

var DeviceBox = React.createClass({
  getInitialState: function() {
    return {current: 0, devices:store.getDevices()};
   },
   updateDevice: function(){
     var state = this.state;
     state.devices = store.getDevices();
     this.setState(state);
   },
   componentDidMount: function() {
     store.addListener(this.updateDevice);
   },
   setDeviceList: function() {
     var state = this.state;
     state.current = 0;
     this.setState(state);
   },
   setAddDevice: function() {
     var state = this.state;
     state.current = 1;
     this.setState(state);
   },
   setUpdateDevice: function(device) {
     var state = this.state;
     state.current = 2;
     state.device = device;
     this.setState(state);
   },

  render: function() {
    var test = <DeviceList devices={this.state.devices} setUpdateDevice={this.setUpdateDevice}/>
    if (this.state.current == 1)
     test = <Device mode="1" setDeviceList={this.setDeviceList}/>
    else if (this.state.current == 2)
      test = <Device mode="2" name={this.state.device.name} setDeviceList={this.setDeviceList} device={this.state.device}/>

      return (
        <div className="deviceBox">
          <DeviceBar onAddDevice={this.setAddDevice}/>
          {test}
        </div>
      );
    }
});

 var TVControl = React.createClass({
         render: function() {
                 return (
                         <div className="tVControl content">
                         TVControl
                         </div>
                 );
         }
  });

  var LightControl = React.createClass({
          render: function() {
                  return (
                          <div className="lightControl content">
                         LightControl
                          </div>
                  );
          }
   });

 var App = React.createClass({
         getInitialState: function() {
                 return {current: <TVControl />,idx:1,side:false,touch_start: null,touch_end: null};
         },
         setMenu: function(menuidx){
           var state = this.state;
           state.idx=menuidx
           if(menuidx == 1)
                 state.current = <TVControl />;
           else if (menuidx == 2)
                   state.current = <LightControl />;
           this.setState(state);
         },
         onTouchStart: function(e){
                 var state = this.state;
                 state.touch_start=e.touches[0]
                 this.setState(state);
         },
         onTouchMove: function(e){
                 var state = this.state;
                 state.touch_end=e.touches[0]
                 this.setState(state);
         },
         touchend: function(e){
                if(this.state.touch_start != null && this.state.touch_end != null) {
                        var state = this.state;
                        dx = this.state.touch_end.screenX - this.state.touch_start.screenX
                        if(dx < -50)
                                state.side = true
                        if(dx > 50)
                                state.side = false
                        state.touch_start = null;
                        state.touch_end = null;
                        this.setState(state);
                }
         },
         setSideMenu: function(){
           var state = this.state;
           state.side=!state.side;
           this.setState(state);
         },
         render: function() {
                 var t = this.state.current;
                 var side = "side-menu";
                 if(this.state.side)
                         side += " side-menu-visible";
                 return (
                         <div className="app" onTouchMove={this.onTouchMove} onTouchEnd={this.touchend} onTouchStart={this.onTouchStart}>
                                 <div className="menu-bar">
                                         <a className='side-menu-bt' onClick={this.setSideMenu} href="#">==</a>
                                 </div>
                                 {t}
                                 <div className={side} onClick={this.setSideMenu}>
                                         <a className={this.state.idx==1?'menu-item active':'menu-item '} onClick={this.setMenu.bind(this, 1)} href="#menu1">TV</a>
                                         <a className={this.state.idx==2?'menu-item active':'menu-item '} onClick={this.setMenu.bind(this,2)} href="#menu2">Lights</a>
                                 </div>
                         </div>
                 );
         }
  });

React.render(
  <App />,
  document.getElementById('content')
);
