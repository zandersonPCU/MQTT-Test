import paho.mqtt.client as mqtt

class MQTT_Client(mqtt.Client):
	
	def __init__(self, server_ip, topics, messages, port=1883, keep_alive=60):
		super().__init__()
		self.ip_address = server_ip
		self.port = port
		self.keep_alive = keep_alive
		self.topics = topics
		self.messages = messages

	def connect(self):
		super().connect(self.ip_address, self.port, self.keep_alive)

	def on_connect(self, client, userData, flags, rc):
		print("Connected with code " + str(rc))

		for topic in self.topics:
			client.subscribe(topic)
		
	def on_message(self, client, userData, msg):
		print("Topic: {} / Message: {}".format(msg.topic, str(msg.payload.decode("UTF-8"))))
		self.messages.put(msg)

	def on_disconnect(self, client, userdata, rc):
		print("Disconnected result code " + str(rc))
		client.loop_stop()



