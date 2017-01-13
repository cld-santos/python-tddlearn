# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = []


class Urls(object):

    def index(self, request):
        return HttpResponse("Hello World!")

    def setup_urls(self):
        global urlpatterns
        urlpatterns.append(url(r'^$', self.index))
