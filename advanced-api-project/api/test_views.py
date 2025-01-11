from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an Author
        self.author = Author.objects.create(name="Test Author")

        # Create a Book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # Create a token for authentication
        self.token = Token.objects.create(user=self.user)

        # Define URLs for testing
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])
    
    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        url = self.book_list_url
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id,
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')
    
    def test_read_book(self):
        """Test reading a single book"""
        url = self.book_detail_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['author']['name'], self.author.name)
    