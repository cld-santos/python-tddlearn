import unittest
from Montadora.Carro import Automovel
from Montadora.TipoCarro import Cabritao
from Montadora.TipoCarro import Esportivo


class Engradado:
    _brejas = []

    def mais_breja(self,breja):
        self._brejas.append(breja)
    def brejas(self):
        return self._brejas

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


    def test_escopo_compartilhado_variavel_sem_self(self):
        _kaiser = Engradado()
        _kaiser.mais_breja('xixi de galinha')
        _kaiser.mais_breja('suor de gordo peludo')

        _amstel = Engradado()

        self.assertTrue(_kaiser.brejas() == _amstel.brejas())

if __name__ == "__main__":
    unittest.main()
