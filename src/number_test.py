import unittest


class number_test(unittest.TestCase):
    def test_somar(self):
        a = 0.1
        b = 0.3
        self.assertTrue(a + b == 0.4)

    def test_multiplicar(self):
        a = 20
        b = 30
        self.assertTrue(a * b == 600)

    def test_dividir(self):
        a = 50
        b = 5
        self.assertTrue(a / b == 10)

    def test_resto_divisao(self):
        a = 5
        b = 2
        self.assertTrue(a % b == 1)

    def test_descartar_fracao(self):
        a = 5
        b = 2
        self.assertTrue(a // b == 2)

    def test_elevar_a_potencia(self):
        a = 5
        b = 2
        self.assertTrue(a ** b == 25)

    def test_progressao_aritmetica(self):
        crescent_numbers = [number for number in range(10)]
        decrescent_numbers = [x for x in range(-10, 0, 1)]
        crescent_pair_numbers = [number for number in range(0, 10, 2)]
        negative_numbers = [number for number in range(0, -10, -1)]

        self.assertEqual(crescent_numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(decrescent_numbers, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])
        self.assertEqual(crescent_pair_numbers, [0, 2, 4, 6, 8])
        self.assertEqual(negative_numbers, [0, -1, -2, -3, -4, -5, -6, -7, -8, -9])


if __name__ == "__main__":
    unittest.main()
