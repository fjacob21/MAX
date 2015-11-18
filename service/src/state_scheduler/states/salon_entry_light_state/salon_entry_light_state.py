import MAX
import time
import datetime
from .off_state import off_state
from .on_state import on_state
from .prio_off_state import prio_off_state
from .prio_on_state import prio_on_state
import urllib2
import urllib
from xml.dom import minidom

class salon_entry_light_state(object):
    def __init__(self):
        self._off_state = off_state(self)
        self._on_state = on_state(self)
        self._prio_off_state = prio_off_state(self)
        self._prio_on_state = prio_on_state(self)
        self.set_state(self._off_state)

    @property
    def name(self):
        return 'Salont entry light state'

    @property
    def description(self):
        return "State machine that control the salon entry light"

    def parseTime(self, timestr):
        parts = timestr.split(' ')
        times = parts[0].split(':')
        hour = int(times[0])
        minute = int(times[1])
        if parts[1] == 'pm':
            hour = hour + 12
        return (hour, minute)

    def getSunInfo(self):
        url = "http://weather.yahooapis.com/forecastrss?w=3534"
    	dom = minidom.parse(urllib.urlopen(url))
    	cond = dom.getElementsByTagName('yweather:astronomy')[0]
    	sunrise = cond.attributes['sunrise'].value
        sunset = cond.attributes['sunset'].value
        return [self.parseTime(sunrise), self.parseTime(sunset)]

    @property
    def sunrise(self):
        return self.getSunInfo()[0]

    @property
    def sunset(self):
        return self.getSunInfo()[1]

    def isMorning(self):
        now = datetime.datetime.now().time()
        isMorning = (datetime.time(6) <= now <= datetime.time(self.sunrise[0],self.sunrise[1]))
        return isMorning

    def isEvening(self):
        now = datetime.datetime.now().time()
        isEvening = (datetime.time(self.sunset[0], self.sunset[1]) <= now <= datetime.time(21, 30))
        return isEvening

    def isLightNeeded(self):
        isLightNeeded = self.isMorning() or self.isEvening()
        return isLightNeeded

    def set_state(self, state):
        self._current_state = state
        self._current_state.enter()

    def event(self, event, source, params):
        #Sprint('Fire {device}.{event}'.format(event=event, device=source.name))
        self._current_state.event(event, source, params)
