# Test driver to test averages.py, random_numbers.py, tables.py

import tables
import random_numbers
import time
from averages import OneMinute, FiveMinute, ThirtyMinute
from datetime import datetime

start = True

# making objects
one_min = OneMinute()
five_min = FiveMinute()
thirty_min = ThirtyMinute()

# initially set values to 0
ave_vales = [0, 0, 0]
while start:
    # application 1 test
    random_val = random_numbers.random_input()
    random_timer = random_numbers.random_timer()

    # application 2 test
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

    # application 3 test
    new_table = tables.add_to_table(ave_vales)
    time.sleep(random_timer)
    print(new_table)


