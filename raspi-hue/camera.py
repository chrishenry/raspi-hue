import picamera
from picamera import BufferIO, PiCamera

def get_image_colors():

    ibuffer = get_image_buffer()

    print ibuffer

def get_image_buffer():

    camera = PiCamera()
    try:
        ibuffer = BufferIO()
        camera.capture(ibuffer, format='jpeg')
    except Exception as e:
        print e
    finally:
        camera.close()

    return ibuffer
