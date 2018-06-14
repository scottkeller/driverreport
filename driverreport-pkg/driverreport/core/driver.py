"""
MODULE: core.driver
DESCRIPTION: Creates and stores driver information and any related trips and statistics

CLASSES:
    Driver
"""

from .trip import Trip


class Driver(object):
    """
    Driver object to store name and trip information

    PROPERTIES:
       name
       trips
       total_distance
       total_time
       avg_speed

    PUBLIC METHODS:
       add_trip
    """

    def __init__(self, name):
        self.name = name
        self.trips = []
        self.total_distance = 0
        self.total_time = 0
        self.avg_speed = 0

    def add_trip(self, start_time, end_time, distance):
        """Adds  trip to the drivers trips"""

        trip = Trip(start_time, end_time, distance)

        # Add trip to driver if the trips average speed vas less than 5mph or greater than 100mph
        trip_speed = self.calc_avg_speed(trip.distance, trip.duration)
        if trip_speed >= 5 and trip_speed <= 100:
            self.trips.append(trip)

            # Calculate the total distance, driving time, and speed as trips are added
            self.total_distance = (self.calc_total_distance(self.trips))
            self.total_time = self.calc_total_time(self.trips)
            self.avg_speed = self.calc_avg_speed(self.total_distance, self.total_time)

    @staticmethod
    def calc_total_distance(trips):
        """Calculates total distance of a list of Trips objects"""
        return int(round(sum([trip.distance for trip in trips])))

    @staticmethod
    def calc_total_time(trips):
        """Calculates total driving time of a driver in minutes"""
        return int(round(sum([trip.duration for trip in trips])))

    @staticmethod
    def calc_avg_speed(distance, time):
        """Calculates average speed in mph given distance in miles and time in minutes"""
        return int(round((distance / float(time)) * 60))

