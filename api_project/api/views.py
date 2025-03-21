from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions
from rest_framework.permissions import  IsAuthenticated,IsAdminUser

from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]