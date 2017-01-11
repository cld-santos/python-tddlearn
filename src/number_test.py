import unittest


class number_test(unittest.TestCase):
    def test_somar(self):
        a = 0.1
        b = 0.3
        self.assertTrue(a + b == 0.4)
        print("test_somar: OK")

    def test_multiplicar(self):
        a = 20
        b = 30
        self.assertTrue(a * b == 600)
        print("test_multiplicar: OK")

    def test_dividir(self):
        a = 50
        b = 5
        self.assertTrue(a / b == 10)
        print("test_dividir:OK")

    def test_resto_divisao(self):
        a = 5
        b = 2
        self.assertTrue(a % b == 1)
        print("test_resto_divisao:ok")


if __name__ == "__main__":
    unittest.main()
