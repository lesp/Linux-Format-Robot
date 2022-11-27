from gpiozero import PWMOutputDevice
from time import sleep
rra = PWMOutputDevice(14,initial_value=0)
rrb = PWMOutputDevice(15,initial_value=0)
lra = PWMOutputDevice(18,initial_value=0)
lrb = PWMOutputDevice(23,initial_value=0)

fra = PWMOutputDevice(24,initial_value=0)
frb = PWMOutputDevice(25,initial_value=0)
fla = PWMOutputDevice(8,initial_value=0)
flb = PWMOutputDevice(7,initial_value=0)

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

def lratest(speed):
    lra.value = speed
    lrb.value = 0
    sleep(2)
    lra.value = 0
    lrb.value = speed


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
sleep(10)
backward(1.0)
sleep(10)
stop()
