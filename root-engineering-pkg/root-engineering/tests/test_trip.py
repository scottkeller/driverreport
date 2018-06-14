"""
MODULE: test_trip.py
DESCRIPTION: Runs unit tests on the trip module
"""

import unittest
from core.trip import Trip

# Constants
TIME_FORMAT = '%H:%M'

class TestTrip(unittest.TestCase):
    """Unit tests for the Trip class"""
    def setUp(self):
        """Sets unit test class property trip to Trip class before each test method call"""
        self.trip = Trip

    def test_trip_exists(self):
        """Tests that the trip property exists"""
        self.assertIsNotNone(self.trip)

    def test_trip_atrrbutes(self):
        """Tests the setting of Trip attributes"""
        mytrip = self.trip('07:00', '07:50', 39.1)
        self.assertEqual(mytrip.start_time.time().strftime(TIME_FORMAT), '07:00')
        self.assertEqual(mytrip.end_time.time().strftime(TIME_FORMAT), '07:50')
        self.assertEqual(mytrip.distance, 39.1)
        self.assertEqual(mytrip.duration, 50)



if __name__ == '__main__':
    unittest.main()
