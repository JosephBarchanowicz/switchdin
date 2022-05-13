import paho.mqtt.client as mqtt
import mqtt_subscribe3
import tables

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Client3")
client.connect(mqttBroker)


start = True

while True:

    message = mqtt_subscribe3.on_message()
    ave_list = message.split()
    map_object = map(int, ave_list)
    ave_vales = list(map_object)
    new_table = tables.add_to_table(ave_vales)
    print(new_table)




