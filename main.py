import tables
import random_numbers
from averages import OneMinute, FiveMinute, ThirtyMinute
import time
from datetime import datetime

start = True
one_min = OneMinute()
five_min = FiveMinute()
thirty_min = ThirtyMinute()

# initially set values to 0
ave_vales = [0, 0, 0]

while start:
    random_val = random_numbers.random_input()
    random_timer = random_numbers.random_timer()

    one_min.add_value(random_val)
    if one_min.check_time() <= datetime.now():
        ave_vales[0] = one_min.get_average()
        one_min.reset()

    five_min.add_value(random_val)
    if five_min.check_time() <= datetime.now():
        ave_vales[1] = five_min.get_average()
        five_min.reset()

    thirty_min.add_value(random_val)
    if thirty_min.check_time() <= datetime.now():
        ave_vales[2] = thirty_min.get_average()
        thirty_min.reset()

    new_table = tables.add_to_table(ave_vales)
    print(new_table)
    time.sleep(random_timer)
