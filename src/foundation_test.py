import unittest


def fibonacci_until(limit):
    fib = []
    a, b = 0, 1
    idx = 0
    while idx < limit:
        fib.append(a)
        a, b = b, a + b
        idx += 1
    return fib


class foundation_test(unittest.TestCase):

    def test_fibonacci(self):
        fib_list = fibonacci_until(10)
        self.assertEqual(fib_list, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
