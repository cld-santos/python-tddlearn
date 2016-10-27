import unittest

class string_test(unittest.TestCase):
    def test_comparacao(self):
        me="same_emas"
        self.assertTrue(me[:4]=="same")
        self.assertTrue(me[0]=='s')
        self.assertTrue(me[5:]=='emas')
        self.assertTrue(me[5:9]=="emas")

    def test_da_pra_alterar_uma_string(self):
        me = "lalala"
        error = False
        try:
            me[6] = "o"
        except:
            error = True

        if not error:
            self.fail("atribuição de string imutavel aconteceu Oo")


    def test_manipulacao_de_strings(self):
        me = "lululu"
        self.assertTrue(len(me)==6)
        self.assertTrue(me.replace("u","a")=="lalala")
        self.assertTrue("a" not in me)
        self.assertTrue("u" in me)




    

if __name__ == "__main__":
    unittest.main()
