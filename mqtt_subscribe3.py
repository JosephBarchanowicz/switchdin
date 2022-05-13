import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("Received message: ", message)
    return message


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Client3")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("AVERAGE")
client.on_message = on_message

time.sleep(60)
client.loop_end()
