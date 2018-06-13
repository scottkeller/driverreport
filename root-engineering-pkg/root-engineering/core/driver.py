from .trip import Trip

class Driver:

     """Driver object to store name and trip information"""
     def __init__(self, name):
         self.name = name
         self.trips = []
         self.total_distance = 0
         self.total_time = 0
         self.avg_speed = None

     def add_trip(self, start_time, end_time, distance):
         """Adds  trip to the drivers trips"""

         trip = Trip(start_time, end_time, distance)
         self.trips.append(trip)

         # Calculate the total distance as trips are added
         self.total_distance = self.calc_total_distance(self.trips)

         # Calculate the total driving time in minutes as trips are added
         self.total_time = self.calc_total_time(self.trips)

     @staticmethod
     def calc_total_distance(trips):
         """Calculates total distance of a list of Trips objects"""
         return sum([trip.distance for trip in trips])

     @staticmethod
     def calc_total_time(trips):
         """Calculates total driving time of a driver in minutes"""
         return sum([trip.duration for trip in trips])