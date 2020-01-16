class Automovel:
    _marca = ""
    _tipo = ""

    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipo = tipo

    def get_marca(self):
        return self._marca

