import unittest
from unittest.mock import Mock


class Event:

    def __init__(self):
        self._events = {}

    def on(self, name, action):
        if name not in self._events.keys():
            self._events[name] = []
        self._events[name].append(action)

    def off(self, name, action):
        self._events[name].remove(action)


    def emit(self, name, paramns):
        for _item in self._events[name]:
            _item(paramns)


class Estoque(Event):

    def __init__(self):
        self._products = []
        super(Estoque, self).__init__()

    def BaixarEstoque(self):
        self.emit("estoque-baixado", self._products)

    def EntrarProduto(self):
        self.emit("produto-adicionado")

    def set_product(self, value):
        self._products.append(value)


class test_Events(unittest.TestCase):

    def test_emitir_evento(self):

        _products = [{'prod_id': 11}]
        _estoque_baixou = Mock()
        _produto_entrou = Mock()

        _meu_estoque = Estoque()
        _meu_estoque.set_product(_products[0])
        _meu_estoque.on("estoque-baixado", _estoque_baixou)
        _meu_estoque.on("produto-adicionado", _produto_entrou)

        _meu_estoque.BaixarEstoque()
        self.assertTrue(_estoque_baixou.called)
        _estoque_baixou.assert_called_with(_products)

        self.assertFalse(_produto_entrou.called)

    def test_remover_evento(self):
        _products = [{'prod_id': 1100}]

        _estoque_baixou = Mock()

        meu_estoque = Estoque()
        meu_estoque.set_product(_products[0])
        meu_estoque.on("estoque-baixado", _estoque_baixou)

        meu_estoque.BaixarEstoque()

        self.assertTrue(_estoque_baixou.called)
        _estoque_baixou.assert_called_with(_products)

        meu_estoque.off("estoque-baixado", _estoque_baixou)

        _estoque_baixou.reset_mock()
        meu_estoque.BaixarEstoque()

        self.assertFalse(_estoque_baixou.called)


if __name__ == "__main__":
    unittest.main()
