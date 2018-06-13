import unittest
from core.trip import Trip

# Constants
TIME_FORMAT = '%H:%M'

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.trip = Trip

    def test_trip_exists(self):
        self.assertIsNotNone(self.trip)

    def test_trip_atrrbutes(self):
        mytrip = self.trip('07:00', '07:50', 39.1)
        self.assertEqual(mytrip.start_time.time().strftime(TIME_FORMAT), '07:00')
        self.assertEqual(mytrip.end_time.time().strftime(TIME_FORMAT), '07:50')
        self.assertEqual(mytrip.distance, 39.1)



if __name__ == '__main__':
    unittest.main()