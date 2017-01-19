from django.test import SimpleTestCase
import http.client

class RoutingTest(SimpleTestCase):
    def test_must_get_index_page(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Hello mãe da foca!")
        con.close()

    def test_must_get_post(self):
        con = http.client.HTTPConnection('localhost:8000')
        con.request('GET', '/sw_development/nodejs/')
        resp = con.getresponse()
        self.assertEqual(resp.read().decode(), "Post de nodejs da categoria sw_development.")
        con.close()
        
