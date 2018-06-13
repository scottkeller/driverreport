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
            self.assertEqual(trip.start_time.time().strftime(TIME_FORMAT), '01:17')
            self.assertEqual(trip.end_time.time().strftime(TIME_FORMAT), '03:21')
            self.assertEqual(trip.distance, 133)
            self.assertEqual(trip.duration, 124)



if __name__ == '__main__':
    unittest.main()