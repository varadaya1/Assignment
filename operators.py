from typing import Iterable, Callable

import math

def mul(x: float, y: float) -> float:
    """Returns the product of x and y."""
    return x * y

def id(x: float) -> float:
    """Returns the input value x unchanged."""
    return x

def eq(x: float, y: float) -> float:
    """Returns 1.0 if x is equal to y, otherwise returns 0.0."""
    return 1.0 if x == y else 0.0

def neg(x: float) -> float:
    """Returns the negation of the input value x."""
    return -x

def add(x: float, y: float) -> float:
    """Returns the sum of x and y."""
    return x + y

def max(x: float, y: float) -> float:
    """Returns the maximum of x and y."""
    return max(x, y)

def lt(x: float, y: float) -> float:
    """Returns 1.0 if x is less than y, otherwise returns 0.0."""
    return 1.0 if x < y else 0.0

def sigmoid(x: float) -> float:
    """Returns the sigmoid function of the input value x."""
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))

def relu(x: float) -> float:
    """Returns the rectified linear unit (ReLU) function of the input value x."""
    return max(0, x)

def inv(x: float) -> float:
    """Returns the inverse of the input value x."""
    return 1.0 / x

def inv_back(x: float, d: float) -> float:
    """Computes the derivative of the inverse function with respect to x."""
    return d * (-1 / (x ** 2))

def relu_back(x: float, d: float) -> float:
    """Computes the derivative of the ReLU function with respect to x."""
    return d if x > 0 else 0.0

def log_back(x: float, d: float) -> float:
    """Computes the derivative of the logarithm function with respect to x."""
    return d / x

def is_close(x: float, y: float) -> float:
    """Returns 1.0 if the absolute difference between x and y is less than 1e-2, otherwise returns 0.0."""
    return 1.0 if abs(x - y) < 1e-2 else 0.0

def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    def mapped(ls: Iterable[float]) -> Iterable[float]:
        return [fn(x) for x in ls]
    return mapped

def negList(ls: Iterable[float]) -> Iterable[float]:
    return map(lambda x: -x)(ls)

def zipWith(fn: Callable[[float, float], float]) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    def zipped(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
        return [fn(x, y) for x, y in zip(ls1, ls2)]
    return zipped

def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return zipWith(lambda x, y: x + y)(ls1, ls2)

def test_mul():
    assert mul(2, 3) == 6
    assert mul(0, 5) == 0
    assert mul(-2, -4) == 8

def test_id():
    assert id(10) == 10
    assert id(0) == 0
    assert id(-5) == -5

# Add tests for other functions similarly

if __name__ == "__main__":
    test_mul()
    test_id()
    # Call other test functions here
