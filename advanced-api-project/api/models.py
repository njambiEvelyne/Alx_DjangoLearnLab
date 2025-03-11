from django.db import models

class Author(models.Model):
  """
  Represents an author in the system

  Fields:
    -name (CharField): Name of the author.

  Relationships:
    -One-to-Many: An author can have multiple books
  """
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name



class Book(models.Model):
  """
  Represents the book in the system.

  Fields:
    -title(CharField): The title of the book.
    -publication_year (IntegerField):
    The year the book was published

  Relationships:
    -ForeignKey: Links each book to a single author.
    -'on_delete=models.CASCADE': If an author is deleted, all their books are deleted as well.
    -`related_name="books"`: Allows reverse lookup from Author to Book (e.g., author.books.all()).
  """
  title = models.CharField(max_length=50)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= "books")

  def __str__(self):
    return f"{self.title} ({self.publication_year}) - {self.author.name}"