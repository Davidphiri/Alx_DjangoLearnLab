from django.contrib import admin
from .models import Book

@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','publication_year']
    list_filter = ['title', 'author','publication_year']
    search_fields = ['title', 'author']