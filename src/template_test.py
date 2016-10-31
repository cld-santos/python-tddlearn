import unittest
from django.template import Template, Context, Engine
from django.conf import settings

class template_test(unittest.TestCase):
    def test_render_a_template(self):
        _engine = Engine() 
        _template = _engine.from_string("Simple replacement {{ target }}.")
        _context = Context({"target":"Claudio Santos"})
        self.assertTrue(_template.render(_context) == "Simple replacement Claudio Santos.")

if __name__ == "__main__":
    import django
    settings.configure(DEBUG=True)
    django.setup()
    unittest.main()
