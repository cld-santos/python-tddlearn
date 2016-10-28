import unittest
from  Montadora import Automovel, Cabritao, Esportivo

class object_test(unittest.TestCase):
    def test_limpando_a_bunda_na_pia(self):
        gol = Automovel("wolksvagen","cabritão")
        gol._marca = "chery" # da mas é que nem limpar a bunda na pia
        
        self.assertTrue(gol.get_marca() == "chery")

    def test_heranca_simples(self):
        gol = Cabritao("Wolksvagen")
        #print(gol.get_marca())
        civic = Esportivo("Honda")
        self.assertTrue(civic.tipo=="Esportivo")

if __name__ == "__main__":
    unittest.main()
