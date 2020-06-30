import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    def test_max_list_iter(self):
        """tests the max_list_iter function"""
        tlist = None
        nlist = []
        int_list1 = [0, 1, 3, 5, 7, 8, 11]
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(max_list_iter(nlist), None)
        self.assertEqual(max_list_iter(int_list1), 11)
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter(list_val), 10)


    def test_reverse_rec(self):
        """tests the reverse_rec function"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        tlist = None
        self.assertEqual(reverse_rec([]), [])
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([0, 3, 7, 9, 13]), [13, 9, 7, 3, 0])


    def test_bin_search(self):
        """tests the bin_search function"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        int_list = None
        int_list1 = [0, 1, 3, 5, 7, 8, 11]
        self.assertEqual(bin_search(7, low, high, list_val), 5)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        with self.assertRaises(ValueError):
            bin_search(3, 0, 3, int_list)
        self.assertEqual(bin_search(11, 0, len(int_list1) - 1, int_list1), 6)


if __name__ == "__main__":
        unittest.main()

    
