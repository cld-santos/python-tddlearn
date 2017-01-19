from django.template import loader, Context
from django.test import SimpleTestCase


class TemplateTest(SimpleTestCase):

    def test_must_fill_a_list(self):
        template = loader.get_template('posts.html')
        filled_template = template.render(Context({
            'page_title': 'testando',
            'posts': [
                {'title': 'Primeiro'},
                {'title': 'Segundo'}
            ]
        }))
        self.assertEqual(filled_template,
                         '<html><head><title>testando</title></head><body><h1>Primeiro</h1><h1>Segundo</h1></body></html>')
