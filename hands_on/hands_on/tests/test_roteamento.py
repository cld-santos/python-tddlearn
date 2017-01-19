from django.test import SimpleTestCase
import http


class RoteamentoTestCase(SimpleTestCase):

    def test_must_get_index(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Hello world!")
        con.close()

    def test_must_get_post(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '/programacao/django_rest_framework/')
        resp = con.getresponse()
        self.assertEqual(
            resp.read().decode(),
            "Post django_rest_framework da categoria programacao"
        )
        con.close()
