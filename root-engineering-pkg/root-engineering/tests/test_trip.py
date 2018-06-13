import unittest
from core.trip import Trip

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.trip = Trip

    def test_trip_exists(self):
        self.assertIsNotNone(self.trip)


if __name__ == '__main__':
    unittest.main()