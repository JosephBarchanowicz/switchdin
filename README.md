# SwitchDin Skills Assessment 

### Tasks

##### 1. Write a random number gernerator in python that publishes a random number between 1 and 100 to an MQTT topic in a message broker on a random interval between 1 and 30 seconds.  

The file mqtt.publish1.py covers this first task.  This file creates a client, Client1, and connects to a broker to publish a random value at a random time to the topic "RANDOM_VAL". This files uses the functions from random_numbers.py to create both the random number and random timer. 

##### 2. Stand up a simple MQTT message broker.  

To stand up a simple MQTT message broker I used "mqtt.eclipseprojects.io".  I do not think this was the best solution and would have to be changed to a more permenant ip based solution before deployment.  

##### 3. A second python application that subscribes to the above message, reads the random number from the broker, and calculates one minute, 5 minute, and 30 minute averages.  These should then be sent back to the broker on a different topic.  

The file mqtt.subscribe2.py creates a client, Client2, and subscribes it to the topic "RANDOM_VAL" and receives the random value from Client1.  The file mqtt.publish2.py creates a new topic "AVERAGE" for Client2, where it takes the random value received from its subscribed topic. It then uses the classes from averages.py to produce the average of the random value every minute, five minutes, and thirty minutes and publishes them to the topic "AVERAGE".  

##### 4. A third python application that subscribes to the statistics calculated in point 3, and prints these out in a pretty tabular layout. 

The file mqtt.subscribe3.py creats a client, Client3, and subscribes it to the topic "AVERAGE" and receives the average values from Client2. The file mqtt.publish3.py then takes the values received from the "AVERAGE" topic and prints them in a pretty tabular layout. It uses the functions from tables.py which in return uses the prettytable library. 




