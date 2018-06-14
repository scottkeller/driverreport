"""
MODULE: test_trip.py
DESCRIPTION: Runs unit tests on the main module
"""

import unittest
from core.main import read_file, driver_report

class TestMain(unittest.TestCase):
    """Tests main module functions"""

    def test_read_file(self):
        """Tests that files can be read and read from relative paths"""
        self.assertIsNotNone(read_file('input.txt'))
        self.assertIsNotNone(read_file('./input.txt'))


    def test_report_from_input(self):
        """Tests that reports are generated as expected"""
        expected_output = "Alex: 42 miles @ 34 mph\nDan: 39 miles @ 47 mph\nBob: 0 miles"
        self.assertEqual(driver_report('./input.txt'), expected_output)



if __name__ == '__main__':
    unittest.main()
