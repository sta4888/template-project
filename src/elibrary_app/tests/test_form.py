from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from ..forms import AddBookForm


class CatalogFormTests(TestCase):
    """ Тесты для форм """

    def setUp(self):
        url = reverse('elibrary_app:home')
        self.response = self.client.get(url)

    def test_book_form(self):
        form = self.response.context.get('add_book_form')
        self.assertIsInstance(form, AddBookForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('add_book_form')
        self.assertIn('class="form-control"', form.as_p())

    def test_book_form_validation_for_blank_items(self):
        add_book_form = AddBookForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability':
                ''}
        )
        self.assertFalse(add_book_form.is_valid())
