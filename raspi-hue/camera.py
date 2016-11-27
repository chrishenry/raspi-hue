from io import BytesIO
from time import sleep
from picamera import PiCamera

def get_image_colors():

    something = get_image_buffer()

    print something

def get_image_buffer():

    my_stream = BytesIO()
    camera = PiCamera()

    camera.led = False
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, 'jpeg')

    return my_stream
