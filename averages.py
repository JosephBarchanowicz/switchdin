from datetime import datetime, timedelta


class OneMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=10)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=10)


class FiveMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=15)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=15)


class ThirtyMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=20)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(seconds=20)






