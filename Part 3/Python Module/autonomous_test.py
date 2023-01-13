import robot

try:
    while True:
        robot.ultra()
except KeyboardInterrupt:
    print("STOP")
    robot.stop()
    exit()