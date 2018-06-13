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
        self.assertEqual(len(mydriver.trips), 1)
        for trip in mydriver.trips:
            self.assertIsInstance(trip, Trip)
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

        for trip in mytrips:
            mydriver.add_trip(trip.start_time.strftime(TIME_FORMAT), trip.end_time.strftime(TIME_FORMAT), trip.distance)

        self.assertEqual(len(mydriver.trips), 3)

        for i, trip in enumerate(mydriver.trips):
            self.assertIsInstance(trip, Trip)
            self.assertEqual(trip.start_time, mytrips[i].start_time)
            self.assertEqual(trip.end_time, mytrips[i].end_time)
            self.assertEqual(trip.distance, mytrips[i].distance)
            self.assertEqual(trip.duration, mytrips[i].duration)





if __name__ == '__main__':
    unittest.main()