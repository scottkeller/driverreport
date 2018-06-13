from .trip import Trip

class Driver:

     """Driver object to store name and trip information"""
     def __init__(self, name):
         self.name = name
         self.trips = []

     def add_trip(self, start_time, end_time, distance):
         trip = Trip(start_time, end_time, distance)
         self.trips.append(trip)