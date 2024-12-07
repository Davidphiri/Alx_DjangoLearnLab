from django.urls import path
from .views import register, user_login, user_logout, list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),  # Registration
    path('login/', user_login, name='login'),      # Login
    path('logout/', user_logout, name='logout'),  # Logout
]
