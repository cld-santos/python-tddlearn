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

 - Pipenv shell
``` bash
$ pipenv shell
```

 - Para testar o código puramente python:
``` bash
$ python -m unittest discover -s src/ -v -p '*_test.py'
```

 - Para testar o código com django
 
``` bash
$ export DJANGO_SETTINGS_MODULE=settings.test
$ export PYTHONPATH=$PYTHONPATH:$PWD
$ cd src
$ python manage.py runserver 0.0.0.0:8000
$ python manage.py test
```



