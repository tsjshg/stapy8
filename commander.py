
import paho.mqtt.client as mqtt
import time
import random
import struct

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

def move():
	cmd = random.choice(['forward','backward','circle'])
	arg = random.choice([10,20,40])
	return '{}:{}'.format(cmd, arg)

def rotate():
	cmd = random.choice(['left','right'])
	arg = random.randint(0,360)
	return '{}:{}'.format(cmd, arg)

def cmd_gen():
	return random.choice([move, rotate])()

while client.loop() == 0:
	client.publish("/tsjshg.info/kame_cmd", cmd_gen(), 0, False)
	time.sleep(2)
