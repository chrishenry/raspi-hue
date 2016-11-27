from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

def get_image_colors(image):

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

    my_stream.seek(0)

    return Image.open(my_stream)


if __name__ == '__main__':
    image = get_image()
    print image
    colors = image.getcolors(maxcolors=1000000)
    colors.sort(key=lambda x: x[0])
    print colors[-10:]
