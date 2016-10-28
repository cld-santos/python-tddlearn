import unittest
from unittest.mock import MagicMock 
from util.EventOriented import Event

class Estoque(Event):

    def BaixarEstoque(self):
        self.emit("estoque-baixado")

    def EntrarProduto(self):
        self.emit("produto-adicionado")


class test_Events(unittest.TestCase):

    def test_emitir_evento(self):

        _estoque_baixou = MagicMock()
        _produto_entrou = MagicMock()
          

        meu_estoque = Estoque()
        meu_estoque.on("estoque-baixado", _estoque_baixou)
        meu_estoque.on("produto-adicionado",_produto_entrou)
        meu_estoque.BaixarEstoque()
        self.assertTrue(_estoque_baixou.called)
        self.assertFalse(_produto_entrou.called)

if __name__ == "__main__":
    unittest.main()
