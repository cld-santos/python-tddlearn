# coding: utf-8
from django.test import SimpleTestCase
import http.client


class UrlTestCase(SimpleTestCase):

    def test_must_access_root_url(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Hello World!")
        con.close()

    def test_access_url_param_url(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '/lalala/lululu/')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Post lululu da lalala.")
        con.close()
