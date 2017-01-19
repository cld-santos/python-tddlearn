from django.test import TestCase
from ..models import Autor, Post


class ModelsBlogTestCase(TestCase):

    def test_must_save_a_author(self):
        author = Autor(name='claudião',
                       temas='programação,software')
        author.save()

        self.assertTrue(len(Autor.objects.all()) == 1)

    def test_must_save_a_blog(self):
        author = Autor(name='claudião',
                       temas='programação,software')
        author.save()

        self.assertTrue(len(Autor.objects.all()) == 1)

        post = Post(titulo='como fazer um churrasco',
                    description='te vira negão',
                    autor=author)
        post.save()

        post = Post(titulo='como pilotar motos',
                    description='capitulo especial: curvas',
                    autor=author)
        post.save()

        self.assertTrue(len(Post.objects.all()) == 2)
