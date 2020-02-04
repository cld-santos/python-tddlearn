import unittest


class string_test(unittest.TestCase):


    def test_comparacao(self):
        me = "same_emas"
        raw_string = r"c:\lalala\alalal"
        non_raw_string = "c:\lalala\alalal"
        self.assertTrue(raw_string != non_raw_string)
        self.assertTrue(me[:4] == "same")
        self.assertTrue(me[0] == 's')
        self.assertTrue(me[5:] == 'emas')
        self.assertTrue(me[5:9] == "emas")

    def test_da_pra_alterar_uma_string(self):
        me = "lalala"
        imutavel = None
        hello = 'hello'

        try:
            hello.upper()
            me[6] = "o"
        except:
            imutavel = True

        self.assertFalse(hello == 'HELLO')
        self.assertTrue(imutavel)

    def test_manipulacao_de_strings(self):
        me = "lululu"
        self.assertTrue(len(me) == 6)
        self.assertTrue(me.replace("u", "a") == "lalala")
        self.assertTrue("a" not in me)
        self.assertTrue("u" in me)


if __name__ == "__main__":
    unittest.main()
