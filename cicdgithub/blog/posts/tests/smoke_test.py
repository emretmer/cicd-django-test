from django.test import TestCase
from django.urls import reverse

class SmokeTest(TestCase):
    def test_homepage_loads(self):
        """
        Ana sayfanın düzgün şekilde yüklenip yüklenmediğini kontrol eder.
        """
        response = self.client.get(reverse('home'))  # Ana sayfanın URL'ini kontrol ediyoruz.
        self.assertEqual(response.status_code, 200)  # Sayfanın 200 OK döndürmesini bekliyoruz.

