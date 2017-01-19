from django.conf.urls import url
from django.http import HttpResponse
from django.template import loader, Context
from blog.models import Autor, Post


def index(request):
    return HttpResponse("Hello mãe da foca!")


def get_post(request, category, post_name):
    db_posts = Post.objects.filter(category__iexact=category)
    context = {'posts': []}

    for post in db_posts:
        context['posts'].append({'titulo': post.titulo})

        template = loader.get_template('posts.html')
        filled_template = template.render(Context(context))

    return HttpResponse(filled_template)


urlpatterns = []
urlpatterns.append(url(
    r'^(?P<category>[a-zA-Z\_]{5,20})/(?P<post_name>[a-zA-Z\_]{5,20})/$',
    get_post))
urlpatterns.append(url(r'^$', index))
