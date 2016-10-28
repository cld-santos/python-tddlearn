import unittest
from Montadora.Carro import Automovel
from Montadora.TipoCarro import Cabritao
from Montadora.TipoCarro import Esportivo

class object_test(unittest.TestCase):
    def test_acessa_variavel_privada(self):
        gol = Automovel("wolksvagen","cabritão")
        gol._marca = "chery" 
        print("da mas é que nem limpar a bunda na pia")
        
        self.assertTrue(gol.get_marca() == "chery")

    def test_heranca_simples(self):
        gol = Cabritao("Wolksvagen")
        civic = Esportivo("Honda")
        self.assertTrue(civic.tipo=="Esportivo")

if __name__ == "__main__":
    unittest.main()
