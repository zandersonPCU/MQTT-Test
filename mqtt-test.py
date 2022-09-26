import MQTTClient
import PiGPIO
import Camera
from queue import Queue
from servo_functions import move_servo

io = PiGPIO.PiGPIO()
messages = Queue()
camera = Camera.Camera()

topics = ["pi/camera", "pi/servo/1/angle", "pi/servo/2/angle", "pi/servo/3/angle", "pi/servo/4/angle"]

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

        match msg.topic:
            case "pi/camera":
                if(msg.payload.decode("utf-8") == "take"):
                    camera.take_picture('/home/pi/Documents/Images')

            case "pi/servo/1/angle":
                angle = int(msg.payload.decode("utf-8"))
                move_servo(0, angle)
                client.publish("pi/servo/1/graph", angle)

            case "pi/servo/2/angle":
                angle = int(msg.payload.decode("utf-8"))
                move_servo(1, angle)
                client.publish("pi/servo/2/graph", angle)

            case "pi/servo/3/angle":
                angle = int(msg.payload.decode("utf-8"))
                move_servo(2, angle)
                client.publish("pi/servo/3/graph", angle)
    
    client.loop_stop()
