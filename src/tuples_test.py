import unittest


class tuples_test(unittest.TestCase):
    def test_criando_tuplas(self):
        yeah = 1, 2, 3, 4
        self.assertTrue(len(yeah) == 4)

    def test_se_append_tuples(self):
        yeah = (1, 2, 3, 4)
        error = False
        try:
            yeah.append(2)
        except:
            error = True

        if not error:
            self.fail("Append em tuple deveria estourar erro!")

    def test_se_tuples_sao_mutaveis(self):
        yeah = (1, 2, 3, 4)
        error = False

        try:
            yeah[2] = 20
        except:
            error = True

        if not error:
            self.fail("Eita... tuplas são imutaveis! isso não deveria ter ocorrido")


if __name__ == "__main__":
    unittest.main()
