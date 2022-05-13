import paho.mqtt.client as mqtt
import random_numbers
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Client1")
client.connect(mqttBroker)

while True:
    random_val = random_numbers.random_input()
    random_timer = random_numbers.random_timer()
    client.publish("RANDOM_VAL", random_val)
    print(f"Just published {random_val} to Topic RANDOM_VAL")
    time.sleep(random_timer)
