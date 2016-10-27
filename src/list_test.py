import unittest

class list_test(unittest.TestCase):
    def test_criar_list_from_string(self):
        wow = "ca ra ka".split(" ")
        self.assertTrue(wow[1] == "ra")

    def test_unir_list(self):
        wow = "ca ra ka".split(" ")
        wow.insert(1,"ra")
        self.assertTrue(''.join(wow) == "cararaka")

    def test_manipular_list(self):
        wow = []

        wow.append("ca")
        wow.append("ra")
        wow.append("ka")
        
        self.assertTrue(''.join(wow) == "caraka")
        wow.pop()
        self.assertTrue(''.join(wow) == "cara")
        
if __name__ == "__main__":
    unittest.main()
