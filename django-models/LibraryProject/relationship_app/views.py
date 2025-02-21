from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # ✅ Import Library and Book models

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Render template

# Class-Based View for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ Correct template path
    context_object_name = "library"  # ✅ Used in template
