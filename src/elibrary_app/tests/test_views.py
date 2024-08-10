from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from elibrary_app.models import Catalog


class CatalogViewTests(TestCase):
    """ Тест для представлений """

    def setUp(self):
        url = reverse('elibrary_app:home')
        self.response = self.client.get(url)

    @patch('elibrary_app.views.get_joke')  # Попробуйте патчить именно здесь
    def test_service_get_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'chuck norris joke'

        url = reverse('elibrary_app:home')
        response = self.client.get(url)

        # Проверка, что шутка отображена на странице
        self.assertIn('chuck norris joke', response.content.decode())

    def test_book_list_view(self):
        Book_1 = Catalog.objects.create(
            title='Django for Beginners (2018)',
            ISBN='978-1-60309-0',
            author='John Doe',
            price=9.99,
            availability='true'
        )
        Book_2 = Catalog.objects.create(
            title='Django for Professionals (2020)',
            ISBN='978-1-60309-3',
            author='Mary Doe',
            price=11.99,
            availability='false'
        )
        url = reverse('elibrary_app:home')
        response = self.client.get(url)
        self.assertIn('Django for Professionals (2020)', response.content.decode())
        self.assertIn('John Doe', response.content.decode())
        self.assertIn('978-1-60309-3', response.content.decode())
