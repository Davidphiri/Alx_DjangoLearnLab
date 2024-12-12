from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"  # Example author name
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library_name = "Central Library"  # Example library name
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    sample_queries()