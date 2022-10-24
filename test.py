import unittest
from main import MaxFinder, the_checker


class TestThree(unittest.TestCase):
    def test_a_biggest(self):
        ob = MaxFinder(3, 2, 1)
        actual = ob.greatest_of_three()
        expected = ("a", [3])
        self.assertEqual(actual, expected)

    def test_b_biggest(self):
        ob = MaxFinder(2, 3, 1)
        actual = ob.greatest_of_three()
        expected = ("b", [3])
        self.assertEqual(actual, expected)

    def test_c_biggest(self):
        ob = MaxFinder(2, 1, 3)
        actual = ob.greatest_of_three()
        expected = ("c", [3])
        self.assertEqual(actual, expected)

    def test_ac_biggest(self):
        ob = MaxFinder(3, 1, 3)
        actual = ob.greatest_of_three()
        expected = ("a i c", [3, 3])
        self.assertEqual(actual, expected)

    def test_bc_biggest(self):
        ob = MaxFinder(1, 3, 3)
        actual = ob.greatest_of_three()
        expected = ("b i c", [3, 3])
        self.assertEqual(actual, expected)

    def test_ab_biggest(self):
        ob = MaxFinder(-1, -1, -3)
        actual = ob.greatest_of_three()
        expected = ("a i b", [-1, -1])
        self.assertEqual(actual, expected)

    def test_abc_biggest(self):
        ob = MaxFinder(-1, -1, -1)
        actual = ob.greatest_of_three()
        expected = ("a, b i c", [-1, -1, -1])
        self.assertEqual(actual, expected)
 
        
class TestLotOfInt(unittest.TestCase):
    def test_many_int_no_rep(self):
        actual = the_checker([-1, -5, 20, 50, 34, 64, 53, 66])
        expected = ("h", "8", 66)
        self.assertEqual(actual, expected)

    def test_many_int_rep(self):
        actual = the_checker([-1, -5, 20, 50, 34, 66, 53, 66])
        expected = ("f, h", "6, 8", 66)
        self.assertEqual(actual, expected)
