from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    """
    Test case for the Book API endpoints.
    """

    def setUp(self):
        """
        Create test data for books and a test user.
        """
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.book1 = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2021)
        self.book2 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)
        self.book3 = Book.objects.create(title="REST APIs with Django", author="Mark Smith", publication_year=2023)
        self.book_url = "/api/books/"

   
    def test_get_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Ensure all books are returned

    
    def test_get_single_book(self):
        response = self.client.get(f"{self.book_url}{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")  # Log in user
        data = {"title": "New Django Book", "author": "John Doe", "publication_year": 2024}
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  # A new book should be added

   
    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized Book", "author": "Unknown", "publication_year": 2025}
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Access denied

    
    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")
        data = {"title": "Updated Title", "author": "William S. Vincent", "publication_year": 2022}
        response = self.client.put(f"{self.book_url}{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f"{self.book_url}{self.book2.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())  # Ensure the book is deleted

   
    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.book_url}?author=Eric Matthes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Eric Matthes")

    
    def test_search_books(self):
        response = self.client.get(f"{self.book_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)  # At least two books should match

    
    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.book_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        publication_years = [book["publication_year"] for book in response.data]
        self.assertEqual(publication_years, sorted(publication_years))  # Should be in ascending order
