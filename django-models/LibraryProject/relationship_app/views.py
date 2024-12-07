from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related('author').all()  # Optimized query with select_related
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Custom template
    context_object_name = 'library'  # The name used in the template context
