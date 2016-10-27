import unittest

class test_dict(unittest.TestCase):
    def test_create_dict(self):
        sheep = {"name":"shaun","breed":"sheep","age":10}
        self.assertTrue(len(sheep)==3)

    def test_access_dict_value_as_attribute(self):
        sheep = {"name":"shaun","breed":"sheep","age":10}
        error = False

        try:
            self.assertTrue(sheep.name=="shaun")
        except:
            error = True

        if not error: 
            self.fail("should be got error")


if __name__ == "__main__":
    unittest.main()
