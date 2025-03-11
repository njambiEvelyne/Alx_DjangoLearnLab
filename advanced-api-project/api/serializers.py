from rest_framework import serializers
from datetime import datetime
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):

  """
    Serializer for the Book model.
    
    Fields:
        - Includes all fields of the Book model (title, publication_year, author).
    
    Validation:
        - Ensures the publication_year is not in the future.
    
    Purpose:
        - Converts Book model instances to JSON format and vice versa.
    """
  class Meta:
    model = Book
    fields = "__all__"

  def validate_publication_year(self, value):
    """Ensure the publication year is not in the future."""
    current_year = datetime.now().year
    if value > current_year:
        raise serializers.ValidationError("Publication year cannot be in the future.")
    return value

class AuthorSerializer(serializers.ModelSerializer):
  """
    Serializer for the Author model.
    
    Fields:
        - name: The name of the author.
        - books: A nested BookSerializer to include related books.
    
    Relationship Handling:
        - Uses `many=True, read_only=True` to serialize multiple books dynamically.
        - Ensures that when an Author instance is retrieved, its books are also included in a structured format.
    
    Purpose:
        - Provides a complete view of an author, including their books.
    """
  books = BookSerializer(many =True, read_only = True)

  class Meta:
    model = Author
    fields = ['name', 'books']