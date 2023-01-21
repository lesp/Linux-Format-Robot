from bluedot import BlueDot
import robot
from signal import pause
from time import sleep
delay = 1
def dpad(pos):
    if pos.top:
        print("Forward")
        robot.forward(0.5)
        sleep(delay)
        robot.stop()
    elif pos.bottom:
        print("Backward")
        robot.backward(0.5)
        sleep(delay)
        robot.stop()
    elif pos.left:
        print("Spinning left")
        robot.spin_left(0.5)
        sleep(delay)
        robot.stop()
    elif pos.right:
        print("Spinnng right")
        robot.spin_right(0.5)
        sleep(delay)
        robot.stop()
    elif pos.middle:
        print("EMERGENCY STOP")
        robot.stop()
        sleep(delay)

bd = BlueDot()
bd.when_pressed = dpad

pause()
