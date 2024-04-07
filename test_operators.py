import unittest
import operators

class TestOperators(unittest.TestCase):
    def test_mul(self):
        # Test cases for multiplication function
        self.assertAlmostEqual(operators.mul(2, 3), 6)
        self.assertAlmostEqual(operators.mul(0, 5), 0)
        self.assertAlmostEqual(operators.mul(-4, 2), -8)
    
    def test_id(self):
        # Test cases for identity function
        self.assertAlmostEqual(operators.id(10), 10)
        self.assertAlmostEqual(operators.id(-5), -5)
    
    # Add more test functions for other operators

if __name__ == '__main__':
    unittest.main()

import unittest
from minitorch.operators import addLists

class TestOperators(unittest.TestCase):
    def test_addLists(self):
        # Test case 1
        ls1 = [1, 2, 3]
        ls2 = [4, 5, 6]
        expected_result = [5, 7, 9]
        self.assertEqual(addLists(ls1, ls2), expected_result)

        # Test case 2
        ls1 = [10, 20, 30]
        ls2 = [40, 50, 60]
        expected_result = [50, 70, 90]
        self.assertEqual(addLists(ls1, ls2), expected_result)

        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()

import unittest
from minitorch.operators import map, negList, zipWith, addLists, reduce, sum, prod

class TestOperators(unittest.TestCase):

    def test_map(self):
        # Test map function
        fn = lambda x: x * 2
        input_list = [1, 2, 3, 4]
        expected_output = [2, 4, 6, 8]
        self.assertEqual(list(map(fn)(input_list)), expected_output)

    def test_negList(self):
        # Test negList function
        input_list = [1, 2, 3, 4]
        expected_output = [-1, -2, -3, -4]
        self.assertEqual(list(negList(input_list)), expected_output)

    def test_zipWith(self):
        # Test zipWith function
        fn = lambda x, y: x + y
        input_list1 = [1, 2, 3, 4]
        input_list2 = [5, 6, 7, 8]
        expected_output = [6, 8, 10, 12]
        self.assertEqual(list(zipWith(fn)(input_list1, input_list2)), expected_output)

    def test_addLists(self):
        # Test addLists function
        input_list1 = [1, 2, 3, 4]
        input_list2 = [5, 6, 7, 8]
        expected_output = [6, 8, 10, 12]
        self.assertEqual(list(addLists(input_list1, input_list2)), expected_output)

    def test_reduce(self):
        # Test reduce function
        fn = lambda x, y: x * y
        start = 1
        input_list = [1, 2, 3, 4]
        expected_output = 24
        self.assertEqual(reduce(fn, start)(input_list), expected_output)

    def test_sum(self):
        # Test sum function
        input_list = [1, 2, 3, 4]
        expected_output = 10
        self.assertEqual(sum(input_list), expected_output)

    def test_prod(self):
        # Test prod function
        input_list = [1, 2, 3, 4]
        expected_output = 24
        self.assertEqual(prod(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()

