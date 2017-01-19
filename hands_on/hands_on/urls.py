from django.conf.urls import url
from django.http import HttpResponse
from django.template import loader, Context
from blog.models import Post


def index(request):
    return HttpResponse('Hello world!')


def get_post(request, category, post_name):
    db_posts = Post.objects.filter(category__iexact=category)
    context = {'page_title': 'hands on django', 'posts': []}

    for post in db_posts:
        context['posts'].append({'title': post.titulo})

        template = loader.get_template('posts.html')
        filled_template = template.render(Context(context))

    return HttpResponse(filled_template)


urlpatterns = []
urlpatterns.append(url(
    r'^(?P<category>[a-zA-Z\_]{5,30})/(?P<post_name>[a-zA-Z\_]{5,30})/$',
    get_post)
)

urlpatterns.append(url(r'^$', index))
