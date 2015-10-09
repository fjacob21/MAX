import time
import sched, time

s = sched.scheduler(time.time, time.sleep)

t = (2015, 10, 7, 22, 33, -1, -1, -1, -1)
#print(time.mktime( t ))
#print(time.localtime(time.mktime( t )))
#print(time.time())
#print(time.localtime())

def print_time(): print "From print_time", time.localtime()
s.enterabs(time.mktime( t ), 1, print_time, ())
#s.enter(5, 1, print_time, ())
#s.enter(10, 1, print_time, ())
s.run()
