from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

def get_image_colors():

    image = get_image_buffer()

    print image
    print image.show()
    print image.histogram()

    return image

def get_image():

    my_stream = BytesIO()
    camera = PiCamera()

    camera.led = False
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, 'jpeg')
    camera.close()

    return Image.open(my_stream)
