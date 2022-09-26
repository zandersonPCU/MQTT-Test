from picamera import PiCamera
from time import sleep
import os

class Camera():

    def __init__(self):
        self.camera = PiCamera()
        self.img_index = 0


    def take_picture(self, save_path):
        save_path = os.path.join(save_path, f"image{self.img_index}.jpg")

        self.camera.start_preview()
        sleep(5)
        self.camera.capture(save_path)
        self.camera.stop_preview()
        # self.camera.close()

        self.img_index += 1