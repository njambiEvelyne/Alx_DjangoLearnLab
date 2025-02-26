from django.contrib import admin
from django.urls import path
from .views import book_list, create_book, edit_book, delete_book, register

path('', book_list, name='book_list'),
path('create/', create_book, name='create_book'),
path('edit/<int:book_id>/', edit_book, name='edit_book'),
path('delete/<int:book_id>/', delete_book, name='delete_book'),
path('register/', register, name='register'),
path('register/', views.register, name='register'),
