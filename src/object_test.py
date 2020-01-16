import unittest
from Montadora.Carro import Automovel
from Montadora.TipoCarro import Esportivo



class object_test(unittest.TestCase):

    def test_acessa_variavel_privada(self):
        gol = Automovel("wolksvagen", "cabritão")
        gol._marca = "chery"  # dá, mas é que nem limpar a bunda na pia")

        self.assertTrue(gol.get_marca() == "chery")

    def test_heranca_simples(self):

        civic = Esportivo("Honda")
        self.assertTrue(civic.tipo == "Esportivo")

    '''
    Quando criamos um objeto temos que ter em mente que uma variavel declarada
    no corpo da classe é compartilhado por todos os objetos, se torna uma
    variável global dentro da classe.
    '''
    def test_escopo_compartilhado_variavel_sem_self(self):
        class Engradado:
            _brejas = []

            def mais_breja(self, breja):
                self._brejas.append(breja)

            def brejas(self):
                return self._brejas

        _kaiser = Engradado()
        _kaiser.mais_breja('lager')
        _kaiser.mais_breja('IPA')

        _amstel = Engradado()

        for x in range(1, len(_kaiser.brejas())):
            self.assertTrue(_kaiser.brejas()[x] == _amstel.brejas()[x])

    def test_endereco_quebrado_por_field_descriptor(self):
        class AddressField(object):
            def __set__(self, instance, full_address):
                broken_address = full_address.split(',')

                setattr(instance, 'full_address', broken_address)
                setattr(instance, 'address_type', broken_address[0].strip())
                setattr(instance, 'address_name', broken_address[1].strip())
                setattr(instance, 'number', broken_address[2].strip())

            def __get__(self, instance, instance_type):
                return instance.full_address

        class Place(object):
            address = AddressField()

        place = Place()
        place.address = "Rua, Jose Carlos da Nobrega, 155"
        self.assertTrue(place.address, "Rua, Jose Carlos da Nobrega, 155")
        self.assertTrue(place.address_type, "Rua")
        self.assertTrue(place.address_name, "Jose Carlos da Nobrega")
        self.assertTrue(place.number, "155")


if __name__ == "__main__":
    unittest.main()
