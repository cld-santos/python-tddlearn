# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = []


class Urls(object):

    def setup_urls(self):
        global urlpatterns
        urlpatterns.append(url(r'^(?P<categoria>[a-z]+)/(?P<post>[a-z]+)/$',
                               self.parametrized_url))
        urlpatterns.append(url(r'^$', self.index))

    def index(self, request):
        return HttpResponse("Hello World!")

    def parametrized_url(self, request, categoria, post):
        return HttpResponse("Post {0} da {1}.".format(post, categoria))
