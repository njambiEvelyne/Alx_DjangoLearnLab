import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Ensure this matches your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Get the author instance
    return Book.objects.filter(author=author)  # Use filter() to get all books by this author

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Get the library instance
    return library.books.all()  # ManyToMany relationship allows direct access

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Get the library instance
    return Librarian.objects.get(library=library)  # Use get() to fetch the librarian

if __name__ == "__main__":
    print("Books by Author:", list(get_books_by_author("J.K. Rowling")))
    print("Books in Library:", list(get_books_in_library("City Library")))
    print("Librarian for Library:", get_librarian_for_library("City Library"))

