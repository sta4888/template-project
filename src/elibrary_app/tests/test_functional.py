from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from ..models import Catalog
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_name_list_functional(self):
        # Create test data
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

        # Simulate user interactions using Selenium
        self.selenium.get(reverse('elibrary_app:home'))
        self.assertIn('E-library Application', self.selenium.title)
        names = self.selenium.find_elements(By.CLASS_NAME, 'card')
        self.assertEqual(len(names), 2)
        # self.assertEqual(names[0].text, 'John - John Doe')
        # self.assertEqual(names[1].text, 'Jane - Jane Smith')
        #
        # # Simulate the page returns a 200
        # self.assertEqual(self.selenium.title, 'Name List')

