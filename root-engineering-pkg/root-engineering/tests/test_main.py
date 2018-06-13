import unittest
from core.main import read_file

class TestMain(unittest.TestCase):

    def test_read_file(self):
        self.assertIsNotNone(read_file('input.txt'))
        self.assertIsNotNone(read_file('./input.txt'))


if __name__ == '__main__':
    unittest.main()