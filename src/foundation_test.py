import unittest


def fibonacci_until(limit):
    fib = []
    a, b = 0, 1
    idx = 0
    while idx <= limit:
        fib.append(a)
        a, b = b, a + b
        idx += 1
    return fib


def fibv2(value):
    if (value in [0, 1]):
        return value
    return fibv2(value - 1) + fibv2(value - 2)

# fibm_cache is evaluated only one time, which makes it possible
# to have it as a parameter with a default value, it's also possible
# to pre-populate the cache
def fibm(value, fibm_cache={}):
    if (value in [0, 1]):
        return value

    if fibm_cache.get(value, None):
        return fibm_cache[value]

    fibm_cache[value] = fibm(value - 1) + fibm(value - 2)
    return fibm_cache[value]


class foundation_test(unittest.TestCase):

    def test_fibonacci(self):
        fib_list = fibonacci_until(10)
        self.assertEqual(fib_list, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fibv2(self):
        self.assertEqual(fibv2(10), 55)

    def test_fibm(self):
        self.assertEqual(fibm(0), 0)
        self.assertEqual(fibm(5), 5)
        self.assertEqual(fibm(10), 55)
