from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book  # Ensure your Book model is imported

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View function to display a list of books.
    Requires 'can_view' permission.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Create book page.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("Edit book page.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("Delete book page.")


