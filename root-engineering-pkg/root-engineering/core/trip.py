import datetime

# Constants
TIME_FORMAT = '%H:%M'

class Trip:
    """Trip object to store driving time and distance"""
    def __init__(self, start_time, end_time, distance):
        self.start_time = datetime.datetime.strptime(start_time, TIME_FORMAT)
        self.end_time = datetime.datetime.strptime(end_time, TIME_FORMAT)
        self.distance = distance
        self.duration = int(round((self.end_time - self.start_time).total_seconds()/60))  #store trip duration in minutes