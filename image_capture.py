from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
#battery check works after testing

me.streamon()

#because it's a continuous streaming, we need to create a while loop
while True:
    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))

    cv2.imshow("Image", img)
    #this is to show the resize image

    cv2.waitKey(1)
