from bluedot import BlueDot
import robot
from signal import pause

bd = BlueDot()
def dpad(pos):
    if pos.top:
        speed = round(pos.distance,2)
        print("Forward:",speed)
        robot.forward(speed)
    elif pos.bottom:
        speed = round(pos.distance,2)
        print("Backward:",speed)
        robot.backward(speed)
    elif pos.left:
        speed = round(pos.distance,2)
        print("Spin Left:",speed)
        robot.spin_left(speed)
    elif pos.right:
        speed = round(pos.distance,2)
        print("Spin Right:",speed)
        robot.spin_right(speed)


bd.when_pressed = dpad
bd.when_moved = dpad
bd.when_released = robot.stop()

pause()
