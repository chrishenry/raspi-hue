from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

def get_image_colors():

    iobytes = get_image_buffer()

    image = Image.open(io.BytesIO(image_data))

    print image

    print image.show()

def get_image_buffer():

    my_stream = BytesIO()
    camera = PiCamera()

    camera.led = False
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, 'jpeg')
    camera.close()

    return my_stream
