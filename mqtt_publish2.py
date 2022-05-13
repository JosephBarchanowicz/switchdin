import paho.mqtt.client as mqtt
from averages import OneMinute, FiveMinute, ThirtyMinute
import time
from datetime import datetime
import mqtt_subscribe2

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Client2")
client.connect(mqttBroker)


start = True

# making objects
one_min = OneMinute()
five_min = FiveMinute()
thirty_min = ThirtyMinute()

# initially set values to 0
ave_vales = [0, 0, 0]
while True:
    rand_val = int(mqtt_subscribe2.on_message())

    one_min.add_value(rand_val)
    if one_min.check_time() <= datetime.now():
        ave_vales[0] = one_min.get_average()
        one_min.reset()

    five_min.add_value(rand_val)
    if five_min.check_time() <= datetime.now():
        ave_vales[1] = five_min.get_average()
        five_min.reset()

    thirty_min.add_value(rand_val)
    if thirty_min.check_time() <= datetime.now():
        ave_vales[2] = thirty_min.get_average()
        thirty_min.reset()

    listToStr = ' '.join(map(str, ave_vales))
    client.publish("AVERAGE", listToStr)
    print(f"Just published {listToStr} to Topic AVERAGE")
    time.sleep(random_timer)
