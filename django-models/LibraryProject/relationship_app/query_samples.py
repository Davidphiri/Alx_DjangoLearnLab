#Query all books by a specific author
books = Book.objects.filter(author= author_name)

#List all books in a library
list_books = Library.objects.all()

#Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library = 'Retreat')