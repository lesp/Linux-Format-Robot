import robot
from time import sleep
delay = 5

for i in range(4):
    robot.slide_left(0.5)
    sleep(5)
    robot.slide_right(0.5)
    sleep(5)
robot.stop()