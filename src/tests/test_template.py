# coding: utf-8
import os
from django.conf import settings
from django.template import Context, Engine
from django.test import SimpleTestCase


class TemplateTestCase(SimpleTestCase):

    def test_render_a_variable_template(self):
        _engine = Engine()
        _template = _engine.from_string("Simple replacement {{ target }}.")
        _context = Context({"target": "Claudio Santos"})
        self.assertTrue(_template.render(_context) == "Simple replacement Claudio Santos.")

    def test_render_a_file_template(self):
        _engine = Engine(dirs=[os.path.join(settings.BASE_DIR, 'template/')])
        _template = _engine.get_template('base.html')
        _context = Context({'name': 'Claudio Santos', 'biograph': 'programmer ancious to learn python'})
        self.assertTrue(_template.render(_context) == "<html><body>Meu Nome é Claudio Santos e sou programmer ancious to learn python</body></html>\n")

    def test_render_a_file_based_on_template(self):
        _engine = Engine(dirs=[os.path.join(settings.BASE_DIR, 'template/')])
        _template = _engine.get_template('my-bio.html')
        _context = Context({'profile': [
            {'company': 'CGI', 'experience': 'arcobjects programmer'},
            {'company': 'Sigma', 'experience': 'GIS Open source programmer'}
        ]})
        self.assertTrue(_template.render(_context).replace("\n", '') == '<html><head>    <title>  Claudio Santos  </title></head><body>        <h2> CGI </h2>    <p> arcobjects programmer </p>    <h2> Sigma </h2>    <p> GIS Open source programmer </p></body></html>')


if __name__ == "__main__":
    pass
