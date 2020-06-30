import unittest
from location import *

class TestLab1(unittest.TestCase):
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(Location("Paris", 48.9, 2.4)), "Location('Paris', 48.9, 2.4)")
        self.assertEqual(repr(Location("Hyderabad", 92.5, 97.8)), "Location('Hyderabad', 92.5, 97.8)")
        self.assertEqual(repr(Location("Helsinki", -20.5, 40.7)), "Location('Helsinki', -20.5, 40.7)")


if __name__ == "__main__":
        unittest.main()

