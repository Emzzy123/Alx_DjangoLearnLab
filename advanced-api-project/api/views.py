from rest_framework import generics
from rest_framework import filters
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter 
from django_filters import rest_framework 

# ListView - Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'author', 'publication_year']
    filterset_fields = None
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']  
    ordering = ['title']

    # Only render JSON to avoid template error in browsable API
    # renderer_classes = [JSONRenderer]

# DetailView - Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView - Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Custom behavior - log the creation of a new book
        print(f"New book created: {serializer.validated_data['title']}")
        serializer.save()

# UpdateView - Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# DeleteView - Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
