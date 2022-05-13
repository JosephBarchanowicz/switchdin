# SwitchDin Skills Assessment 

### Breif summary on each file and how that are used to achieve the tasks

##### 1. Write a random number gernerator in python that publishes a random number between 1 and 100 to an MQTT topic in a message broker on a random interval between 1 and 30 seconds.  

* The file mqtt.publish1.py covers this first task.  This file creates a client, Client1, and connects to a broker to publish a random value at a random time to the topic "RANDOM_VAL". This files uses the functions from random_numbers.py to create both the random number and random timer. 

##### 2. Stand up a simple MQTT message broker.  

* To stand up a simple MQTT message broker I used "mqtt.eclipseprojects.io".  I do not think this was the best solution and will need to be changed to a more permenant self-hosting solution before deployment.  

##### 3. A second python application that subscribes to the above message, reads the random number from the broker, and calculates one minute, 5 minute, and 30 minute averages.  These should then be sent back to the broker on a different topic.  

* The file mqtt.subscribe2.py creates a client, Client2, and subscribes it to the topic "RANDOM_VAL" and receives the random value from Client1.  The file mqtt.publish2.py creates a new topic "AVERAGE" for Client2, where it takes the random value received from its subscribed topic. It then uses the classes from averages.py to produce the average of the random value every minute, five minutes, and thirty minutes and publishes them to the topic "AVERAGE".  

##### 4. A third python application that subscribes to the statistics calculated in point 3, and prints these out in a pretty tabular layout. 

* The file mqtt.subscribe3.py creats a client, Client3, and subscribes it to the topic "AVERAGE" and receives the average values from Client2. The file mqtt.publish3.py then takes the values received from the "AVERAGE" topic and prints them in a pretty tabular layout. It uses the functions from tables.py which in return uses the prettytable library.   

### How the application should be ran

The applications need to be ran in order as to produce the 1) random number, 2) average values list, 3) print the table. The order the applications need to be ran are as follows:

1) mqtt_publish1.py
2) mqtt_subscribe2.py
3) mqtt_publish2.py
4) mqtt_subscribe3.py
5) mqtt_publish3.py

* note mqtt_publish2.py will publish 0 for each of the average values until the appropriate time frame is reached, then will update the values each time frame is reached after the initial timeframe.   

### Changes needed before implementation 

1) Change the broker from "mqtt.eclipseprojects.io" to a self-hosting broker in the following files:
* mqtt_publish1.py
* mqtt_subscribe2.py
* mqtt_publish2.py
* mqtt_subscribe3.py
* mqtt_publish3.py

2) mqtt_publish3.py is currently only printing to the console, if need to publish to broker then need to change and add a new topic.
3) Remove main.py, this is only a test driver to test the classes and functions used in the publish files. 




