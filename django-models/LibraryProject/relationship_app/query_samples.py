from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)   # ✅ required format
print(f"Books by {author_name}:", books_by_author)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:", books_in_library)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)   # ✅ required format
print(f"Librarian of {library_name}:", librarian)
