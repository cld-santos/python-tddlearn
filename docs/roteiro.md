## Roteiro hands on django

### Roteamento
1. Criar pasta principal do hands_on;
2. Criar manage.py
  ``` python
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
  ```
3. Executar o manage.py check e deixar estourar o erro
4. Criar o arquivo settings
  ``` python 
    # @manage.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hands_on.settings.main")
  ```

  ``` python
    # @hands_on/settins/main.py
    import os
    DEBUG = True
    ALLOWED_HOSTS = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = 'local'
  ```
5. Executar o manage.py check sem erros
6. Criar módulo de teste de roteamento (sem esquecer o __init__.py) e escrever um teste
7. Configurar uma url:
  ``` python
    # @hands_on/settins/main.py
    ROOT_URLCONF="hands_on.urls"
  ```
  ``` python
    # @hands_on/urls.py
    from django.conf.urls import url
    from django.http import HttpResponse
  ```

8. Criar o teste
  ``` python
    def test_must_access_root_url(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Hello World!")
        con.close()
  ```
9. Criar teste parametros especificados na url
  - *Não esqueça do parametro request*

### Teamplate
1. Definindo o config do template
  ``` python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, "templates"),
            ],
        },
    ]
  ```
2. Cria a pasta de templates e construa alguns; 
  - lembre-se de construir um template em uma unica linha, para facilitar o assert;

2. Valide se o template está sendo carregado corretamente;
  - `from django.template import loader` para carregar os templates com o `loader.get_template('<nome_do_template>.<extensão>')`

3. Faça uma substituição no template;
  - `from django.template import Context` para construir o objeto que substituirá as tags (ele recebe um dict com parametro)

4. Faça uma construção de uma lista;
  - `{% %}` tag para inserir código de repetição como um `for`

### Models
1. Construir Database
2. Configurar o settings
``` python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'hands_on',
          'USER': 'postgres',
          'PASSWORD': 'postgres',
          'HOST': '127.0.0.1',
          'PORT': '5432',
      }
  }

  INSTALLED_APPS = (
      'hands_on'
  )
```
3. Construa um modelo simples de autor
4. Construa um modelo de posts com uma foreign key 
5. Execute o makemigrations
6. Apresente as migrations criadas
7. Apresente o banco
8. Execute o migrate
9. Apresente o banco

## Fechamento

1. Mostrar a pagina que renderiza o template