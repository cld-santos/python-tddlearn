from django.core.management.base import BaseCommand
from ...models import Autor, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        author = Autor(name='claudião',
                       temas='programação,software')
        author.save()

        post = Post(titulo='como fazer um churrasco',
                    description='te vira negão',
                    autor=author)
        post.save()

        post = Post(titulo='como pilotar motos',
                    description='capitulo especial: curvas',
                    autor=author)
        post.save()
