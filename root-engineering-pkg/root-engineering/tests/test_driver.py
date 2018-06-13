import unittest
from core.driver import Driver
from core.trip import Trip

# Constants
TIME_FORMAT = '%H:%M'

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.driver = Driver

    def test_driver_exists(self):
        self.assertIsNotNone(self.driver)

    def test_driver_name(self):
        self.assertEqual(self.driver('Scott').name, 'Scott')

    def test_add_single_trip(self):
        mydriver = Driver('Scott')
        mydriver.add_trip('01:17', '3:21', 133)

        #There should now be 1 trip
        self.assertEqual(len(mydriver.trips), 1)

        #Make sure the trip os added to mydriver with the correct values
        self.assertIsInstance(mydriver.trips[0], Trip)
        self.assertEqual(mydriver.trips[0].start_time.time().strftime(TIME_FORMAT), '01:17')
        self.assertEqual(mydriver.trips[0].end_time.time().strftime(TIME_FORMAT), '03:21')
        self.assertEqual(mydriver.trips[0].distance, 133)
        self.assertEqual(mydriver.trips[0].duration, 124)

    def test_multiple_trips(self):
        mydriver = Driver('Scott')
        mytrips = [
                    Trip('02:30', '13:54' ,855),
                    Trip('14:30', '14:31', 1.5),
                    Trip('11:11', '12:24', 70)
                ]
        # Add each trip defined above to mydriver
        for trip in mytrips:
            mydriver.add_trip(trip.start_time.strftime(TIME_FORMAT), trip.end_time.strftime(TIME_FORMAT), trip.distance)
        #There should now be 3 trips
        self.assertEqual(len(mydriver.trips), 3)

        # Ensure trip values match for the defined trips and the trips of mydriver
        for i, trip in enumerate(mydriver.trips):
            self.assertIsInstance(trip, Trip)
            self.assertEqual(trip.start_time, mytrips[i].start_time)
            self.assertEqual(trip.end_time, mytrips[i].end_time)
            self.assertEqual(trip.distance, mytrips[i].distance)
            self.assertEqual(trip.duration, mytrips[i].duration)

    def test_total_distance(self):
        mydriver = Driver('Scott')

        # Total distance should be 0 if there are no trips
        self.assertEqual(mydriver.total_distance, 0)

        mydriver.add_trip('01:00', '1:20', 21)

        # Total distance should now be 21
        self.assertEqual(mydriver.total_distance, 21)

        mydriver.add_trip('11:00', '12:20', 81)

        # Total distance should now be 102
        self.assertEqual(mydriver.total_distance, 102)

    def test_total_time(self):
        mydriver = Driver('Scott')

        # Total time should be 0 if there are no trips
        self.assertEqual(mydriver.total_time, 0)

        mydriver.add_trip('01:00', '1:20', 21)

        # Total time should now be 20
        self.assertEqual(mydriver.total_time, 20)

        mydriver.add_trip('11:00', '12:20', 81)

        # Total time should now be 100
        self.assertEqual(mydriver.total_time, 100)

    def test_avg_speed(self):
        mydriver = Driver('Scott')

        self.assertEqual(mydriver.avg_speed, 0)

        mydriver.add_trip('07:15', '07:45', 17.3)

        self.assertEqual(mydriver.avg_speed, 35)

        mydriver.add_trip('06:12', '06:32', 21.8)

        self.assertEqual(mydriver.avg_speed, 47)




if __name__ == '__main__':
    unittest.main()