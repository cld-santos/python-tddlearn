import unittest
from sys import getrefcount


class ReferenceCountTest(unittest.TestCase):

    def test_must_increase_when_pass_to_nested_methods(self, refcount=[]):

        first_var = [2]
        refcount = 2

        self.assertEqual(getrefcount(first_var), refcount)

        def increasing_ref_count(values):
            result = 0
            sub_refcount = refcount
            sub_refcount += 1; second_var = first_var

            sub_refcount += 1; self.assertEqual(getrefcount(first_var), sub_refcount)

            for value in first_var:
                sub_refcount += 1; self.assertEqual(getrefcount(first_var), sub_refcount)
            sub_refcount -= 1

            self.assertEqual(getrefcount(first_var), sub_refcount)
            return value

        refcount += 1; increasing_ref_count(first_var)
        refcount -= 1; self.assertEqual(getrefcount(first_var), refcount)
