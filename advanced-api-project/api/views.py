from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books.
    - Allows unauthenticated users to access (public read access).
    - Uses Django REST Framework's ListAPIView to handle GET requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a specific book by its ID.
    - Accessible to unauthenticated users (public read access).
    - Uses RetrieveAPIView to fetch a single book record.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    - Restricted to authenticated users only.
    - Uses CreateAPIView to handle POST requests.
    - Validates duplicate book titles before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the default create method to include additional validation.
        If a book with the same title exists, it prevents duplicate entries.
        """
        title = serializer.validated_data.get("title")
        if Book.objects.filter(title=title).exists():
            return Response({"error": "A book with this title already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    - Restricted to authenticated users only.
    - Uses UpdateAPIView to handle PUT/PATCH requests.
    """ 

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow updates only to authenticated users

    def perform_update(self, serializer):
        """
        Custom update logic to enforce permission restrictions.
        """
        instance = self.get_object()
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    - Restricted to authenticated users only.
    - Uses DestroyAPIView to handle DELETE requests.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[permissions.IsAuthenticated]
