# Copyright (c) 2014 Quanyang Liu
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Use OpenCV to get the video from drone.
And use libardrone to control it.
"""

import numpy as np
import cv2
import libardrone

PATH = 'tcp://192.168.1.1:5555'

def main():
    cap = cv2.VideoCapture(PATH)
    
    drone = libardrone.ARDrone()
    
    while cap.isOpened:
        ret, frame = cap.read()

        try:
            cv2.imshow('frame', frame)
        except:
            print "Some error has occured!"
            drone.reset()
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            drone.halt()
            break
        # emergency
        elif key == ord('r'):
            drone.reset()
        # takeoff / land
        elif key == 10:
            drone.takeoff()
        elif key == 32:
            drone.land()
            # forward / backward
        elif key == ord('w'):
            drone.move_forward()
        elif key == ord('s'):
            drone.move_backward()
            # left / right
        elif key == ord('a'):
            drone.move_left()
        elif key == ord('d'):
            drone.move_right()
            # up / down
        elif key == 65362:
            drone.move_up()
        elif key == 65364:
            drone.move_down()
            # turn left / turn right
        elif key == 65361:
            drone.turn_left()
        elif key == 65363:
            drone.turn_right()

        # change camera
        elif key == ord('t'):
            drone.change_camera()
            # speed
        elif key == ord('1'):
            drone.speed = 0.1
        elif key == ord('2'):
            drone.speed = 0.2
        elif key == ord('3'):
            drone.speed = 0.3
        elif key == ord('4'):
            drone.speed = 0.4
        elif key == ord('5'):
            drone.speed = 0.5
        elif key == ord('6'):
            drone.speed = 0.6
        elif key == ord('7'):
            drone.speed = 0.7
        elif key == ord('8'):
            drone.speed = 0.8
        elif key == ord('9'):
            drone.speed = 0.9
        elif key == ord('0'):
            drone.speed = 1.0
            
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
