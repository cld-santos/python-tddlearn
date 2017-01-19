

## Principis motivadores
    - Compartilhamento de conhecimento
    - "Quem ensina aprende ao ensinar" Paulo Freire

## Python TDDLearn (link github)[https://github.com/cld-santos/python-tddlearn]
    Aprendizagem guiada por testes.

## Meus 50 cents sobre django.

    É importante entender algumas coisas do mundo python antes iniciar no django:
     - Python Enhancement Proposal: se é necessário uma evolução no python saporra é feita por meio de uma pep, porém há (peps de padrão de escrita de código)[https://www.python.org/dev/peps/pep-0008/], (padrão para um webserver)[https://www.python.org/dev/peps/pep-0333/] e etc.
     - PIP python package index, gestor de depências do python
     - Python é (strong, dynamic typed)[https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language];
     - Python tem aspectos funcionais como first class function, lambdas;
     - Python é orientada a objetos
     - Python permite herança multipla

### Usamos python3, e daí?
    Usamos python3 nesta demonstração, principalmente pq eu quis estar aderente ao que de mais novo é utilizado e pra entender quais são as principais diferenças
     - sendo elas, todas strings são unicode, neste exemplo não fica evidente, porém é um saco ter que controlar se a string é str ou unicode, isso gera grandes problemas ao lidar com regex leitura de arquivos texto e demais operações com string.
     - facilidade no processamento concorrente/paralelo;
     - processamento assíncrono;

## Django
    Django é um framework web MVT model view template desenvolvido em python.
    Facilitar a publicação de conteúdo, bastante utilizado por jornais provedores de conteúdo, hj pelo insta, pinterest, globo.com

    o que me impressiona:
    1. Perfeita aderência ao protocolo http com roteamento de urls parametrizados para acessar views.
    2. Componentização em um nível que induz os desenvolvedores à criar componentes que possam ser facilmentes incluídos em qualquer outro site django.
    3. Linha de comando pra tudo, pra testar, pra subir o site, pra fazer uma migrate e etc.
    4. Framework de Template
    5. ORM com Migrations
    6. Module de testes
    7. Tem uma baita comunidade ativa fazendo muitas coisas legais e pela facilidade de adoção fica massa demais incorporar libs de terceiros.
    8. Além de td isso temos webservers como tornado ready to event loop e processamento assíncrono

    o que me desagrada:
    1. Tem um belo settings de configuração do framework, parte chata não gosto nada sou mto mais fã de um padrão que o porfa sempre fala e que a M$ e o Ruby on rails tbm usa, fugiu a porra do nome(Porém eu não tenho uma sugestão melhor então fico na minha);
    2. Não ter a possibilidade de escrever o mesmo código para o client e server.

    Com td isso vc pode fazer mta mandraquisse... e contruir mta coisa boua, coisas simples como este blog que vc tá lendo ou o instagram ou pinterest, além de uma porrada de portal e site de noticias.

## Visão organizada:

### Dando nomes aos bois:
    **Projeto**: é o código fonte completo do site.
    **Apps**: é uma pasta na raiz do projeto, onde encontramos os models, templates e views de um projeto
    **Packages**: é uma pasta contendo o arquivo __init__.py, contendo uma coleção de modules
    **Modules**: é um arquivo .py, que pode conter classes ou functions puras.

### Estrutura de um Projeto Django
<nome_do_projeto>/
    <apps_um>/
        template/
            app_template.html
        views.py
        models.py
    <apps_um>/
        template/
            app_template.html
        views.py
        models.py
    static/
        img/
        css/
        js/
    manage.py

### Roteamento de urls
    Views: as views são o elo entre um url roteada e o código que fará a geração do conteúdo que a url representa.

### Template
Permite construir arquivos html com {% notações %} que possibilita renderizar conteúdo sem que seja necessário escrever código complexo para escrever sequencias de html, por exemplo uma tabela.
 - *Podemos trocar a engine de template*

### ORM
    Migrations: Escreva seus models e através dos comandos makemigrations e migrate. construa seu modelo baseado no código que vc escreveu, sem a necessidade de escrever código sql.
    Model: Modulo que permite escrever seus models, determinar relacionamentos como one-to-many,one-to-one e many-to-many;
    QuerySet: Módulo que traz um pacote de ferramentas para consulta de dados de um modelo;


## Rest framework      // Fica para a próxima
    Auth_provider
    Viewset
    Serializers

