from django.urls import path
from . import views

urlpatterns = [
    # Route for listing all books
    path('books/', views.BookListView.as_view(), name='book-list'),

    # Route for retrieving a single book by ID
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Route for creating a new book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),

    # Route for updating an existing book
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),

    # Route for deleting a book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
