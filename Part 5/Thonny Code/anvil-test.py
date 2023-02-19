import robot
import anvil.server
from signal import pause
import time
anvil.server.connect("ANVIL SERVER UPLINK KEY HERE")

@anvil.server.callable
def stop():
    robot.stop()
    print("Done")

@anvil.server.callable
def forward():
    robot.forward(0.5)
    print("Moving forward")

@anvil.server.callable
def backward():
    robot.backward(0.5)
    print("Moving backward")

@anvil.server.callable
def left():
    robot.spin_left(0.5)
    time.sleep(0.5)
    robot.stop()
    print("Spin Left")

@anvil.server.callable
def right():
    robot.spin_right(0.5)
    time.sleep(0.5)
    robot.stop()
    print("Spin Right")

@anvil.server.callable
def dance():
    for i in range(3):
        print("Forward")
        robot.forward(0.5)
        time.sleep(2)
        print("Spin Right")
        robot.spin_right(0.5)
        time.sleep(1)
        robot.stop()
        time.sleep(0.5)



pause()