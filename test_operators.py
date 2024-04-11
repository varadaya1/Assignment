# operators_test.py
import operators

def test_mul():
    assert operators.mul(2, 3) == 6
    assert operators.mul(0, 5) == 0
    assert operators.mul(-4, 2) == -8

def test_id():
    assert operators.id(10) == 10
    assert operators.id(-5) == -5

# addLists_test.py
from operators import addLists

def test_addLists():
    # Test case 1
    ls1 = [1, 2, 3]
    ls2 = [4, 5, 6]
    expected_result = [5, 7, 9]
    assert addLists(ls1, ls2) == expected_result

    # Test case 2
    ls1 = [10, 20, 30]
    ls2 = [40, 50, 60]
    expected_result = [50, 70, 90]
    assert addLists(ls1, ls2) == expected_result

# operators_advanced_test.py
from operators import map, negList, zipWith, addLists, reduce_func, sum, prod

def test_map():
    # Test map function
    fn = lambda x: x * 2
    input_list = [1, 2, 3, 4]
    expected_output = [2, 4, 6, 8]
    assert list(map(fn)(input_list)) == expected_output

def test_negList():
    # Test negList function
    input_list = [1, 2, 3, 4]
    expected_output = [-1, -2, -3, -4]
    assert list(negList(input_list)) == expected_output

def test_zipWith():
    # Test zipWith function
    fn = lambda x, y: x + y
    input_list1 = [1, 2, 3, 4]
    input_list2 = [5, 6, 7, 8]
    expected_output = [6, 8, 10, 12]
    assert list(zipWith(fn)(input_list1, input_list2)) == expected_output

def test_addLists_advanced():
    # Test addLists function
    input_list1 = [1, 2, 3, 4]
    input_list2 = [5, 6, 7, 8]
    expected_output = [6, 8, 10, 12]
    assert list(addLists(input_list1, input_list2)) == expected_output

def test_reduce():
    # Test reduce function
    fn = lambda x, y: x * y
    start = 1
    input_list = [1, 2, 3, 4]
    expected_output = 24
    assert reduce_func(fn, start, input_list) == expected_output

def test_sum():
    # Test sum function
    input_list = [1, 2, 3, 4]
    expected_output = 10
    assert sum(input_list) == expected_output

def test_prod():
    # Test prod function
    input_list = [1, 2, 3, 4]
    expected_output = 24
    assert prod(input_list) == expected_output
