
from django.urls import path
from .views import (
    list_books, LibraryDetailView, 
    admin_view, librarian_view, member_view
)

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("admin-panel/", admin_view, name="admin_view"),
    path("librarian-panel/", librarian_view, name="librarian_view"),
    path("member-panel/", member_view, name="member_view"),
]
