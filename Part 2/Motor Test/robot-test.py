from gpiozero import PWMOutputDevice
from time import sleep
rra = PWMOutputDevice(14,initial_value=0) #right rear motor terminal a
rrb = PWMOutputDevice(15,initial_value=0) #right rear motor terminal b
lra = PWMOutputDevice(18,initial_value=0) #left rear motor terminal a
lrb = PWMOutputDevice(23,initial_value=0) #left rear motor terminal b

fra = PWMOutputDevice(24,initial_value=0) #front right motor terminal a
frb = PWMOutputDevice(25,initial_value=0) #front right motor terminal b
fla = PWMOutputDevice(8,initial_value=0) #front left motor terminal a
flb = PWMOutputDevice(7,initial_value=0) front left motor terminal b

def forward(speed):
    rra.value = speed
    rrb.value = 0
    lra.value = speed
    lrb.value = 0
    fla.value = speed
    flb.value = 0
    fra.value = speed
    frb.value = 0

def backward(speed):
    rra.value = 0
    rrb.value = speed
    lra.value = 0
    lrb.value = speed

    fla.value = 0
    flb.value = speed
    fra.value = 0
    frb.value = speed

def spin_left(speed):
    rra.value = speed
    rrb.value = 0
    lra.value = 0
    lrb.value = speed
    fla.value = 0
    flb.value = speed
    fra.value = speed
    frb.value = 0

def spin_right(speed):
    rra.value = 0
    rrb.value = speed
    lra.value = speed
    lrb.value = 0
    fla.value = speed
    flb.value = 0
    fra.value = 0
    frb.value = speed

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

forward(1.0)
sleep(5)
backward(1.0)
sleep(5)
spin_left(1.0)
sleep(5)
spin_right(1.0)
sleep(5)
stop()
