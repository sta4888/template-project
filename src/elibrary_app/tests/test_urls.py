from django.test import TestCase, SimpleTestCase
from ..models import Catalog
from django.urls import reverse
from django.urls.base import resolve
from ..views import home


class ElibraryURLsTest(SimpleTestCase):
    """ Тестируем URLs """

    def test_homepage_url_name(self):
        # проверка работоспособности урл адреса
        response = self.client.get(reverse('elibrary_app:home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resloves_to_homepage_view(self):
        # проверяем что корневой урл правильно сопоставлен с view функцией
        found = resolve('/elib/')
        self.assertEqual(found.func, home)
