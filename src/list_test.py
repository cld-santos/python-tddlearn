import unittest


class list_test(unittest.TestCase):

    def test_criar_list_from_string(self):
        wow = "ca ra ka".split(" ")
        self.assertTrue(wow[1] == "ra")

    def test_unir_list(self):
        wow = "ca ra ka".split(" ")
        wow.insert(1, "ra")
        self.assertTrue(''.join(wow) == "cararaka")

    def test_manipular_list(self):
        wow = []

        wow.append("ca")
        wow.append("ra")
        wow.append("ka")

        self.assertTrue(''.join(wow) == "caraka")
        wow.pop()
        self.assertTrue(''.join(wow) == "cara")

    def test_list_bidimensionais(self):
        wow = [[1, 2, 3], [2, 3, 4]]
        for item in wow:
            self.assertTrue(len(item) == 3)
            for subitem in item:
                print(subitem)

    def test_list_are_mutable(self):
        wow = ['1', 2, '3', '4']
        wow[1] = "lalala"
        self.assertTrue(''.join(wow) == "1lalala34")

    def test_delete_a_range(self):
        wow = [1, 2, 3, 4]
        del wow[1:3]
        self.assertEqual(wow, [1, 4])

if __name__ == "__main__":
    unittest.main()
