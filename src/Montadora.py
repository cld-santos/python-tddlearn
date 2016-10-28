class Automovel:
    _marca = ""
    _tipo = ""

    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipo = tipo
    def get_marca(self):
        return self._marca

class Cabritao(Automovel):
    def __init__(self,marca):
        super().__init__(marca,"Cabritao")

class Esportivo(Automovel):
    def __init__(self,marca):
        super().__init__(marca,"Esportivo")

    @property
    def tipo(self):
        return self._tipo

