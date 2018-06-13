from .trip import Trip

class Driver:

     """Driver object to store name and trip information"""
     def __init__(self, name):
         self.name = name
         self.trips = []
         self.total_distance = 0
         self.avg_speed = None

     def add_trip(self, start_time, end_time, distance):
         trip = Trip(start_time, end_time, distance)
         self.trips.append(trip)
         # Calculate the total distance as trips are added
         self.total_distance = self.calc_total_distance(self.trips)

     @staticmethod
     def calc_total_distance(trips):
         return sum([trip.distance for trip in trips])