from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Import Library model

# Function-Based View for listing books
def list_books(request):
    books = Book.objects.all()  # ✅ Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Ensure correct template path

# Class-Based View for library details
class LibraryDetailView(DetailView):
    model = Library  # ✅ Define the model
    template_name = "relationship_app/library_detail.html"  # ✅ Ensure correct template path
    context_object_name = "library"  # ✅ Name for template context
