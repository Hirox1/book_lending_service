from django.test import TestCase
from .models import Author

class AuthorTestCase(TestCase):
    def test_create_author(self):
        author = Author.objects.create(name="Test Author")
        self.assertEqual(author.name, "Test Author")
