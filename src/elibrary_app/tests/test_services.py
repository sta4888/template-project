from django.test import SimpleTestCase
from  unittest.mock import patch

from elibrary_app.services import get_joke

class TestServices(SimpleTestCase):

    @patch('elibrary_app.services.get_joke')
    def test_service_get_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(mock_get_joke.return_value, 'one')
