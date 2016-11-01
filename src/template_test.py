import os
import unittest
from django.template import Template, Context, Engine
from django.conf import settings


class template_test(unittest.TestCase):
    def test_render_a_variable_template(self):
        _engine = Engine() 
        _template = _engine.from_string("Simple replacement {{ target }}.")
        _context = Context({"target":"Claudio Santos"})
        self.assertTrue(_template.render(_context) == "Simple replacement Claudio Santos.")

    def test_render_a_file_template(self):
        _engine = Engine(dirs=['/home/ubuntu/src/template/'])
        _template = _engine.get_template('base.html')
        _context = Context({'name': 'Claudio Santos', 'biograph':'programmer ancious to learn python'})
        self.assertTrue(_template.render(_context)=="<html><body>Meu Nome é Claudio Santos e sou programmer ancious to learn python</body></html>\n")

    def test_render_a_file_based_on_template(self):
        _engine = Engine(dirs=['/home/ubuntu/src/template/'])
        _template = _engine.get_template('my-bio.html')
        _context = Context({'profile': [
            {'company': 'CGI', 'experience':'arcobjects programmer'},
            {'company': 'Sigma', 'experience':'GIS Open source programmer'}
        ]})
        self.assertTrue(_template.render(_context).replace("\n",'')=='<html><head>    <title>  Claudio Santos  </title></head><body>        <h2> CGI </h2>    <p> arcobjects programmer </p>    <h2> Sigma </h2>    <p> GIS Open source programmer </p></body></html>')


if __name__ == "__main__":
    import django
    settings.configure(DEBUG=True)
    django.setup()
    unittest.main()
