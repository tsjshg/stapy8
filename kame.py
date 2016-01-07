import paho.mqtt.client as mqtt
import turtle

def on_message(client, userdata, msg):
	print(msg.payload)
	cmd = msg.payload.decode('utf-8').split(':')
	getattr(client.kame, cmd[0])(int(cmd[1]))

def make_kame():
	turtle.setup(400,400)
	kame = turtle.Turtle()
	kame.shape('turtle')
	kame.shapesize(2,2,3)
	return kame

client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883)
client.subscribe('/tsjshg.info/kame_cmd')
client.kame = make_kame()

while client.loop() == 0:
	pass
