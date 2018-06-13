import unittest
from core.driver import Driver

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.driver = Driver

    def test_driver_exists(self):
        self.assertIsNotNone(self.driver)


if __name__ == '__main__':
    unittest.main()