import MQTTClient
import PiGPIO
import time
import RPi.GPIO as GPIO
from queue import Queue

io = PiGPIO.PiGPIO()
messages = Queue()

topics = ["pi/pin7/output"]

client = MQTTClient.MQTT_Client("127.0.0.1", topics, messages)

client.connect()
io.define_output(7)

#Infinite loop to check for messages from MQTT_Client
while True:
    # Need to use loop_start and loop_stop functions to prevent blocking
    # in order to process MQTT_Client messages
    client.loop_start()

    #Loops through the messages queue and processes any unprocessed messages
    while not messages.empty():
        msg = messages.get()

        # if msg.topic == "pi/pin7/output" and msg.payload.decode("UTF-8") == "on":
        #     client.publish('pi/pin7/status', "Pin is on")
        # elif msg.topic == "pi/pin7/output" and msg.payload.decode("UTF-8") == "off":
        #     client.publish('pi/pin7/status', "Pin is off")

        if msg.topic == "pi/pin7/output" and msg.payload.decode("UTF-8") == "on":
            client.publish('pi/pin7/led', True)
            io.set_pin(7, True)
        elif msg.topic == "pi/pin7/output" and msg.payload.decode("UTF-8") == "off":
            client.publish('pi/pin7/led', False)
            io.set_pin(7, False)

        print(io.read_pin(7))

    client.loop_stop()



