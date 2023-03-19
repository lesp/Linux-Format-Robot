from gpiozero import PWMOutputDevice, Button, MotionSensor, DistanceSensor
from time import sleep
rra = PWMOutputDevice(14,initial_value=0) #right rear motor terminal a
rrb = PWMOutputDevice(15,initial_value=0) #right rear motor terminal b
lra = PWMOutputDevice(18,initial_value=0) #left rear motor terminal a
lrb = PWMOutputDevice(23,initial_value=0) #left rear motor terminal b

fra = PWMOutputDevice(24,initial_value=0) #front right motor terminal a
frb = PWMOutputDevice(25,initial_value=0) #front right motor terminal b
fla = PWMOutputDevice(8,initial_value=0) #front left motor terminal a
flb = PWMOutputDevice(7,initial_value=0) #front left motor terminal b

obs = MotionSensor(4)
sensor = DistanceSensor(27, 17)


def forward(speed):
    rra.value = speed
    rrb.value = 0
    lra.value = speed
    lrb.value = 0
    fla.value = speed
    flb.value = 0
    fra.value = speed
    frb.value = 0
    print("Forward")

def backward(speed):
    rra.value = 0
    rrb.value = speed
    lra.value = 0
    lrb.value = speed
    fla.value = 0
    flb.value = speed
    fra.value = 0
    frb.value = speed
    print("Backward")

def spin_left(speed):
    rra.value = speed
    rrb.value = 0
    lra.value = 0
    lrb.value = speed
    fla.value = 0
    flb.value = speed
    fra.value = speed
    frb.value = 0
    print("Spin Left")

def spin_right(speed):
    rra.value = 0
    rrb.value = speed
    lra.value = speed
    lrb.value = 0
    fla.value = speed
    flb.value = 0
    fra.value = 0
    frb.value = speed
    print("Spin Right")

def stop():
    rra.value = 0
    rrb.value = 0
    lra.value = 0
    lrb.value = 0
    fla.value = 0
    flb.value = 0
    fra.value = 0
    frb.value = 0
    print("ALL STOP")

def make_space():
    print("stop")
    stop()
    sleep(1)
    print("backward")
    backward(0.5)
    sleep(1)
    print("stop")
    stop()
    sleep(1)
    print("spin left")
    spin_left(0.5)
    sleep(0.2)
    print("stop")
    stop()
    
def slide_right(speed):
    rra.value = speed
    rrb.value = 0
    lra.value = 0
    lrb.value = speed
    fla.value = speed
    flb.value = 0
    fra.value = 0
    frb.value = speed
    print("Spin Right")

def impact():
    print("IMPACT")
    stop()
    backward(0.5)
    sleep(2)

def obstacle():
   print("Checking for object")
   obs.when_motion = stop

def ultra():
    distance = round(sensor.distance*100,2)
    print('Distance to nearest object is', distance, 'cm')
    if distance < 15:
        make_space()
    else:
        forward(0.5)
    
        



