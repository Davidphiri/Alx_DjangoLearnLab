from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
from .views import BookViewSet

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
