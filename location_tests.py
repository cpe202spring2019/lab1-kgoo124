import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq_diff_locations(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("LA", 35.3, -120.7)
        

        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc3)

    def test_eq_diff_lat(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 55.3, -120.7)
        

        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc3)

    def test_eq_diff_lon(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.3, -129.7)
        

        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc3)


    def test_eq_edge_cases(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = 2
        loc3 = Location("LA", 25.3, -145.2)
        loc4 = Location("LA", 35.3, -110.7)
        

        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc3)
        self.assertNotEqual(loc1, loc4)



if __name__ == "__main__":
        unittest.main()
