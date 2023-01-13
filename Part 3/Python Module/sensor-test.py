from gpiozero import Button
from signal import pause
import robot
button = Button(2)
button.when_pressed = robot.impact

pause()
