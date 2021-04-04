from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
#battery check works after testing

me.takeoff()
me.send_rc_control(0, 30, 0, 0) #move forward
sleep(2)
me.send_rc_control(0, 0, 0, 60) #rotation movement
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()
#test is successful

