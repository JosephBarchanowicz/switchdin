import random


def random_input():
    return random.randint(1, 100)


def random_timer():
    return random.randint(1, 3)


def random_values():
    return [random_input(), random_timer()]
