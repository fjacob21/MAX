var store = devicesStore();
var scripts = scriptsStore();
var eventGenerator = eventGenerator();
var salonlightdoor = device('Salonlightdoor');
var bedlightdesk = device('Bedlightdesk');
var salonlightcorner = device('Salonlightcorner');

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
        loadCommentsFromServer: function() {
                salonlightdoor.light.state({}, this.updateLightState, this.updateError);
                bedlightdesk.light.state({}, this.updateLightState, this.updateError);
                salonlightcorner.light.state({}, this.updateLightState, this.updateError);
        },
        updateLightState: function(data){
                var state = this.state;
                if(data.device.name == 'Salonlightdoor')
                        state.salon_entry = data.state;
                else if(data.device.name == 'Salonlightcorner')
                        state.salon_corner = data.state;
                else if(data.device.name == 'Bedlightdesk')
                        state.bedroom_desk = data.state;

                this.setState(state);
        },
        updateError: function(data){
                console.log("Error:" + data);
        },
        getInitialState: function() {
                return {salon_entry: false, salon_corner: false, bedroom_desk: false};
        },
        componentDidMount: function() {
                this.loadCommentsFromServer();
                setInterval(this.loadCommentsFromServer, 500);
        },
        frontdoor: function() {
                eventGenerator.sendEvent('salon_entry_bt');
        },
        frontdoorReset: function() {
                eventGenerator.sendEvent('salon_entry_reset_bt');
        },
        saloncorner: function() {
                eventGenerator.sendEvent('salon_corner_bt');
        },
        beddesk: function() {
                eventGenerator.sendEvent('bedroom_desk_bt');
        },
        render: function() {
          return (
                  <div className="lightControl content">
                          <a className="content-item" onClick={this.frontdoor} href="#frontdoor">Front door {this.state.salon_entry}</a>
                          <a className="content-item" onClick={this.frontdoorReset} href="#frontdoorReset">Front door reset</a>
                          <a className="content-item" onClick={this.saloncorner} href="#saloncorner">Salon corner{this.state.salon_corner}</a>
                          <a className="content-item" onClick={this.beddesk} href="#bedroomdesk">Bedroom desk{this.state.bedroom_desk}</a>
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
                                         <a className='side-menu-bt glyphicon glyphicon-asterisk' onClick={this.setSideMenu} href="#"></a>
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
