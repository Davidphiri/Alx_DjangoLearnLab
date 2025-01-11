from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return []

# List all books in a library
from relationship_app.models import Library

def list_books_in_library(library_name):
    try:
        # Get the library object by name
        library = Library.objects.get(name=library_name)
        
        # Assuming the library has a related set of books, you can list them
        books = library.books.all()  # Modify according to your actual model relationship
        for book in books:
            print(f"Book Title: {book.title}, Author: {book.author.name}, Published: {book.publication_date}")
    except Library.DoesNotExist:
        print(f"Library with name '{library_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.librarian
    return None

# Sample usage
if __name__ == "__main__":
    # Example data setup (if not using Django admin)
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="John Doe", library=library)

    # Queries
    print("Books by J.K. Rowling:", query_books_by_author("J.K. Rowling"))
    print("Books in Central Library:", list_books_in_library("Central Library"))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
