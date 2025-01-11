from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend  # For filtering
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

# Book filter class for advanced filtering
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Filter by title (case-insensitive)
    author = filters.CharFilter(lookup_expr='icontains')  # Filter by author (case-insensitive)
    publication_year = filters.NumberFilter()  # Filter by publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # Fields available for filtering


# Book List View with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Enable filters, search, and ordering
    filterset_class = BookFilter  # Use the custom filter class defined above
    search_fields = ['title', 'author']  # Enable search on title and author fields
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication_year
    ordering = ['title']  # Default ordering by title

