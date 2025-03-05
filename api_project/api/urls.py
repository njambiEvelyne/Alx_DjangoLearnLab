from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # path('books/', BookList.as_view(), name='book-list'),  # API endpoint for listing books
    path('', include(router.urls)),
]
