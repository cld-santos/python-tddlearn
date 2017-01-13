# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = None


class Urls(object):

    def setup_urls(self):
        global urlpatterns
        # urlpatterns.append(url(r'^(?P<categoria>[a-z]+)/(?P<post>[a-z]+)/$', self.parametrized_url))
        # urlpatterns.append(url(r'^$', self.index))
        urlpatterns = (
            url(r'^(?P<categoria>[a-z]+)/(?P<post>[a-z]+)/$', self.parametrized_url, name='parametrized_url'),
            url(r'^$', self.index, name='index'),
        )

    def index(self, request):
        return HttpResponse("Hello World!")

    def parametrized_url(self, request, categoria, post):
        return HttpResponse("Post {0} da {1}.".format(post, categoria))
