from Montadora.Carro import Automovel


class Cabritao(Automovel):
    def __init__(self,marca):
        super().__init__(marca,"Cabritao")

class Esportivo(Automovel):
    def __init__(self,marca):
        super().__init__(marca,"Esportivo")

    @property
    def tipo(self):
        return self._tipo


