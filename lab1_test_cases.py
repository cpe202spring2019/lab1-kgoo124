import unittest
from lab1 import *

class TestLab1(unittest.TestCase):
    
    def test_max_list_iter_diff_num(self):
        """tests cases when all numbers are different"""
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [1,3,2]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [3,1,2]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_iter_two_same(self):
        "tests cases when two numbers are the same"""
        tlist = [1,3,3]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [3,3,1]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [3,1,3]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [1,1,3]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [1,3,1]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [3,1,1]
        self.assertEqual(max_list_iter(tlist),3) 

    def test_max_list_iter_all_same(self):
        """tests cases when all numbers are the same"""
        tlist = [3,3,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_iter_edge_cases(self):
        """tests if list is None and if list is empty"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    
    def test_reverse_rec(self):
        """test various cases and orientations of the list"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,3]),[3,1,1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec(["a","b","c"]), ["c","b","a"])


    def test_reverse_rec_edge_cases(self):
        """tests if list is None, if list is empty, and if length of list is 1"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        
        tlist = []
        self.assertEqual(reverse_rec(tlist),[])
        tlist = [1]
        self.assertEqual(reverse_rec(tlist),[1])

    
    def test_bin_search_all_values_in_list(self):
        """test all values in a list of 11 elements"""
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2 )
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5 )
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 6 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )

    def test_bin_search_diff_highs_and_lows(self):
        """test cases where low and high don't cover the whole list"""
        list_val = [0, 1, 2, 3, 4]
        self.assertEqual(bin_search(4, 0, 2, list_val), None )
        self.assertEqual(bin_search(0, 2, 3, list_val), None )

    def test_bin_search_edge_cases(self):
        """test edge cases where list is None or list is empty"""
        list_val = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(5, 0, 10, list_val)

        list_val = []
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), None )
       
        list_val = [0]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        list_val =[0, 1]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )



if __name__ == "__main__":
        unittest.main()

    
