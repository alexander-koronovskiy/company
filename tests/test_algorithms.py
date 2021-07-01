from algorithms.binary_search import binary_search
from algorithms.fibonacchi import fib_rec
from algorithms.linear_search import linear_search
from algorithms.quicksort import quick_sort


def test_binary_search():
    assert not binary_search([1, 2, 3, 5, 8], 6)
    assert binary_search([1, 2, 3, 5, 8], 5)


def test_fibonacchi():
    assert fib_rec(10) == 55


def test_linear_search():
    assert linear_search([1, 8, 9, -10, 64], -10)


def test_quick_sort():
    assert quick_sort([1, 8, 9, -10, 64])
