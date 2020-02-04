import unittest


class tuples_test(unittest.TestCase):
    def test_criando_tuplas(self):
        yeah = 1, 2, 3, 4
        self.assertTrue(len(yeah) == 4)

    def test_append_tuples(self):
        yeah = (1, 2, 3, 4)
        error = False
        try:
            yeah.append(2)
        except:
            error = True

        self.assertTrue(error)

    def test_tuples_imutaveis(self):
        yeah = (1, 2, 3, 4)
        error = False

        try:
            yeah[2] = 20
        except:
            error = True

        self.assertTrue(error)

    def test_pack_unpacking(self):
        pack = 1, 2, 'a', 'b'
        x, y, w, z = pack
        self.assertEqual(y, pack[1])
        self.assertEqual(z, pack[3])

if __name__ == "__main__":
    unittest.main()
