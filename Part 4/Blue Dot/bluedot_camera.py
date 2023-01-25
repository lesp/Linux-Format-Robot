from bluedot import BlueDot
from picamera2 import Picamera2, Preview
from libcamera import controls
from signal import pause
import time
bd = BlueDot()
picam2 = Picamera2()

def take_picture():
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (1280, 720)}, display="lores")
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL, x=100, y=200, width=1280, height=720)
    picam2.start(show_preview=True)
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
    time.sleep(2)
    picam2.capture_file("picam1.jpg")
    picam2.stop_preview()
    picam2.stop()
bd.when_pressed = take_picture
pause()
