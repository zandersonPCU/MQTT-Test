import RPi.GPIO as GPIO

"""A class that wraps the RPi.GPIO class to simplify controlling the pi's GPIO"""
class PiGPIO():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
    

    """Sets the designated GPIO pin number to be an output pin"""
    def define_output(self, pin_num):
        GPIO.setup(pin_num, GPIO.OUT)

    """Sets the designated GPIO pin number to be an input pin"""
    def define_input(self, pin_num):
        GPIO.setup(pin_num, GPIO.IN)

    """Returns the value of the designated input pin number"""
    def read_pin(self, pin_num):
        return GPIO.input(pin_num)

    """Sets the output level of the designated output pin (Can be HIGH(True) or LOW(False))"""
    def set_pin(self, pin_num, state):
        GPIO.output(pin_num, state)