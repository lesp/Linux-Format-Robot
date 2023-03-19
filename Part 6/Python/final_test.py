import robot
from time import sleep
delay = 5
try:
    while True:
        robot.ultra()
        sleep(delay)
except (RuntimeError, KeyboardInterrupt):
    print("STOP")
    robot.stop()
    exit()