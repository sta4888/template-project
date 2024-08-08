from django.test import TestCase
from ..models import Catalog


class CatalogModelTests(TestCase):
    """ Тест модели каталога """
    def setUp(self):
        # выполняет действие, которое запускается перед каждым тестовым методом
        # создаем экземпляр Catalog с определенными полями
        self.book = Catalog(
            title='First Django Book',
            ISBN='978-1-60309-3',
            author='Ilya Perminov',
            price='9.99',
            availability='True'
        )


    def test_create_book(self):
        # проверяем, действительно ли новая запись является экземпляром модели Catalog
        self.assertIsInstance(self.book, Catalog)


    def test_str_representation(self):
        self.assertEqual(str(self.book), "First Django Book")


    def test_saving_and_retrieving_book(self):
        # можем ли мы получить, так и сохранить новую книгу в каталоге
        first_book = Catalog()
        first_book.title = 'First Django Book'
        first_book.ISBN = '978-1-60309-3'
        first_book.author = 'Ilya Perminov'
        first_book.price = '9.99'
        first_book.availability = 'True'
        first_book.save()
        second_book = Catalog()
        second_book.title = 'Second Django Book'
        second_book.ISBN = '978-3-60124-1'
        second_book.author = 'Dmitry Seleznev'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()
        saved_books = Catalog.objects.all()
        self.assertEqual(saved_books.count(), 2)
        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'First Django Book')
        self.assertEqual(second_saved_book.author, 'Dmitry Seleznev')
