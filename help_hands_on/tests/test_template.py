from django.template import loader, Context
from django.test import SimpleTestCase


class TemplateTest(SimpleTestCase):

    def test_must_load_a_template(self):
        template = loader.get_template('post_detail.html')
        self.assertTrue(template is not None)

    def test_must_fill_a_template(self):
        template = loader.get_template('post_detail.html')
        filled_template = template.render(Context({
            'titulo': 'Meu Post',
            'descricao': 'minha descrição do meu post'}))

        self.assertEqual(filled_template,
                         '<html><body><h1>Meu Post</h1><p>minha descrição do meu post</p></body></html>')

    def test_must_fill_a_list(self):
        template = loader.get_template('posts.html')
        filled_template = template.render(Context({
            'posts': [
                {'titulo': 'Primeiro'},
                {'titulo': 'Segundo'}
            ]
        }))

        self.assertEqual(filled_template,
                         '<html><body><h1>Primeiro</h1><h1>Segundo</h1></body></html>')
