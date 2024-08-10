from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class CatalogTemplateTests(TestCase):
    """ Тест шаблона """

    def setUp(self):
        url = reverse('elibrary_app:home')
        self.response = self.client.get(url)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'elibrary_app/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'E-library Application')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hello World')
