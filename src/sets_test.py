import unittest


class sets_test(unittest.TestCase):
    def test_criando_sets(self):
        yeah = {1, 2, 3, 4, 4}
        self.assertTrue(len(yeah) == 4)

    def test_if_append_set(self):
        yeah = {1, 2, 3, 4}
        error = False
        try:
            yeah.append(2)
        except:
            error = True

        self.assertTrue(error)

    def test_se_sets_sao_mutaveis(self):
        #Tuplas sao mutaveis, Sets que nao sao.
        yeah = {1, 2, 3, 4}
        error = False
        try:
            yeah[2] = 20
        except:
            error = True

        self.assertTrue(error)

    def test_intercection_operation(self):

        sets_a = {1, 2, 3, 4}
        sets_b = {3, 4, 5, 6}
        intersection = sets_a & sets_b
        self.assertTrue(len(intersection) == 2)
        self.assertEqual(intersection, {3, 4})

    def test_diference_operation(self):

        sets_a = {1, 2, 3, 4}
        sets_b = {3, 4, 5, 6}
        intersection = sets_a - sets_b
        self.assertTrue(len(intersection) == 2)
        self.assertEqual(intersection, {1, 2})

if __name__ == "__main__":
    unittest.main()
