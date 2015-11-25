var store = new devicesStore();
var scripts = new scriptsStore();
var events = new eventGenerator();
var salonlightdoor = new device('Salonlightdoor');
var bedlightdesk = new device('Bedlightdesk');
var salonlightcorner = new device('Salonlightcorner');

var LightUnitControl = React.createClass({
        loadLightState: function() {
                this.props.device.light.state({}, this.updateLightState, this.updateError);
        },
        updateLightState: function(data){
                var state = this.state;
                state.state = data.state;
                this.setState(state);
        },
        updateError: function(data){
                console.log("Error:" + data);
        },
        onClick: function() {
                events.sendEvent(this.props.event);
        },
        getInitialState: function() {
                return {state: false};
        },
        componentDidMount: function() {
                this.loadLightState();
                setInterval(this.loadLightState, 500);
        },
         render: function() {
                 var state = 'ON';
                 if(this.state.state == false)
                        state = 'OFF';
                 return (
                         <div className="lightUnitControl content-item" onClick={this.onClick}>
                                 <div className="lightUnitControlItem glyphicon glyphicon-lamp"></div>
                                 <a className="lightUnitControlItem" href="#frontdoor">{this.props.description}</a>
                                 <div className="lightUnitControlItem">{state}</div>
                         </div>
                 );
         }
  });

var TVControl = React.createClass({
         wakeup: function() {
                 scripts.execute('openhouse', '1');
         },
         close: function() {
                 scripts.execute('closehouse', '1')
         },
         render: function() {
                 return (
                         <div className="tVControl content">
                                 <a className="content-item" onClick={this.wakeup} href="#wakeup">Wakeup</a>
                                 <a className="content-item" onClick={this.close} href="#close">Close</a>
                         </div>
                 );
         }
  });

var LightControl = React.createClass({
        frontdoorReset: function() {
                events.sendEvent('salon_entry_reset_bt');
        },
        all: function() {
                events.sendEvent('salon_entry_bt');
                events.sendEvent('salon_corner_bt');
                events.sendEvent('bedroom_desk_bt');
        },
        render: function() {
          return (
                  <div className="lightControl content">
                          <LightUnitControl description="Front Door" event='salon_entry_bt' device={salonlightdoor}/>
                          <a className="content-item" onClick={this.frontdoorReset} href="#frontdoorReset">Front door reset</a>
                          <LightUnitControl description="Salon corner" event='salon_corner_bt' device={salonlightcorner}/>
                          <LightUnitControl description="Bedroom desk" event='bedroom_desk_bt' device={bedlightdesk}/>
                          <a className="content-item" onClick={this.all} href="#all">All</a>
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
                 state.touch_start=e.touches[0].screenX;
                 this.setState(state);
         },
         onTouchMove: function(e){
                 var state = this.state;
                 state.touch_end=e.touches[0].screenX;
                 this.setState(state);
         },
         touchend: function(e){
                var state = this.state;
                if(this.state.touch_start != null && this.state.touch_end != null) {
                        var dx = this.state.touch_end - this.state.touch_start;
                        if(dx < -50)
                                state.side = true
                        if(dx > 50)
                                state.side = false
                }
                state.touch_start = null;
                state.touch_end = null;
                this.setState(state);
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
                                         <a className='glyphicon glyphicon-menu-hamburger side-menu-bt' onClick={this.setSideMenu} href="#"></a>
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

ReactDOM.render(
  <App />,
  document.getElementById('content')
);
