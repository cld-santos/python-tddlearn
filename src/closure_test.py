import unittest


class ClosureTest(unittest.TestCase):

    def test_enclosing_var_should_exist_in_nested_func(self):

        message = ["a", "b", "c"]

        def iterate_over_message():
            result = ""
            for text in message:
                result += text + " "

            return result
        self.assertEqual(iterate_over_message(), "a b c ")

    def test_enclosing_var_in_nested_func_is_read_only(self):

        message = "abc"

        def mess_with_message():
            message += "d"
            result = ""
            for text in message:
                result += text + " "
            return result

        error = True
        try:
            mess_with_message()
            error = False
        except:
            pass

        self.assertTrue(error)


