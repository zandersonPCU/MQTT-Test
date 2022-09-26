import MQTTClient
import PiGPIO
import RPi.GPIO as GPIO
import Camera
from queue import Queue

io = PiGPIO.PiGPIO()
messages = Queue()
camera = Camera.Camera()

topics = ["pi/pin7/output", "pi/camera", "pi/servo/1/angle", "pi/servo/2/angle", "pi/servo/3/angle", "pi/servo/4/angle"]

client = MQTTClient.MQTT_Client("127.0.0.1", topics, messages)

client.connect()
io.define_output(4)


#Infinite loop to check for messages from MQTT_Client
while True:
    # Need to use loop_start and loop_stop functions to prevent blocking
    # in order to process MQTT_Client messages
    client.loop_start()

    #Loops through the messages queue and processes any unprocessed messages
    while not messages.empty():

        msg = messages.get()

        client.handle_message(msg, client, io, camera)


    client.loop_stop()







