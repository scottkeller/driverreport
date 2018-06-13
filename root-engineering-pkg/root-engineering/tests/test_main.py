import unittest
from core.main import read_file, driver_report

class TestMain(unittest.TestCase):

    def test_read_file(self):
        self.assertIsNotNone(read_file('input.txt'))
        self.assertIsNotNone(read_file('./input.txt'))


    def test_report_from_input(self):
        expected_output = "Alex: 42.0 miles @ 34 mph\nDan: 39.1 miles @ 47 mph\nBob: 0 miles"
        self.assertEqual(driver_report('./input.txt'), expected_output)



if __name__ == '__main__':
    unittest.main()