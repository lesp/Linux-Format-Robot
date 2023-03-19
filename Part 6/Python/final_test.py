import robot
from time import sleep
delay = 1
try:
    while True:
        robot.ultra()
        sleep(5)
except KeyboardInterrupt:
    print("STOP")
    robot.stop()
    exit()