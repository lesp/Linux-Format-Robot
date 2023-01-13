from gpiozero import Button
from signal import pause

def bump():
    print("Impact")

button = Button(2)

button.when_pressed = bump

pause()
