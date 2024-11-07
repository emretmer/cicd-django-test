from django.test import TestCase
from django.urls import reverse

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        # '/hello/' URL'sine GET isteği gönder
        response = self.client.get(reverse('hello_world'))
        
        # HTTP status kodunun 200 olduğunu kontrol et
        self.assertEqual(response.status_code, 200)
        
        # Yanıt içeriğinin 'Hello, World!' olduğunu kontrol et
        self.assertContains(response, "Hello, World!")
