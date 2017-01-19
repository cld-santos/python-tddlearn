# python-tddlearn

O objetivo principal deste repositório é divulgar minha estratégia de aprendizado.

Em resumo eu sigo as práticas do tdd para conduzir meu aprendizado.

Desta forma se eu quero validar uma caracteristica específica de um recurso da linguagem eu faço:

``` python
    def test_comparacao(self):
        me = "same_emas"
        self.assertTrue(me[:4] == "same")
        self.assertTrue(me[0] == 's')
        self.assertTrue(me[5:] == 'emas')
        self.assertTrue(me[5:9] == "emas")
```

**Temporáriamente o código do hands_on está neste repositório, enquanto não disponibilizamos o repositório oficial do chat do caos**


[**Link apresentação**](https://youtu.be/G2IK3oAnXS0)



 - Start do ambiente:
``` bash
$ sudo apt-get install git vagrant
$ git clone git@github.com:cld-santos/python-tddlearn.git
$ cd python-tddlearn
$ vagrant up
$ vagrant provision
$ vagrant ssh
```

 - Para testar o código puramente python:
``` bash
$ python3 -m unittest discover -s src/ -v -p '*_test.py'
```

 - Para testar o código com django
``` bash
$ cd src
$ python3 manage.py runserver 0.0.0.0:8000
$ python3 manage.py test
```



