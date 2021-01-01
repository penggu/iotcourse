import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(3)
    camera.stop_preview()
    camera.capture('image.jpg') # Capturing image to a file
    camera.start_recording('my_video.h264') # Start recording to a file
    camera.wait_recording(5)  # Records the video for given time
    camera.stop_recording() # Stop recording
    # More examples:
    # camera.capture(my_stream, 'jpeg') # Capturing to a stream
    # camera.start_recording(stream, quantization=23) # Recording to a stream

