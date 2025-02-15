# Deleting the Book Instance

### Command:
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())  # Checking if any books remain
