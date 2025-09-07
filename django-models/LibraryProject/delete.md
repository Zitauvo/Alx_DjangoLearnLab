# Delete Operation

```python
from bookshelf.models import Book

# Retrieve and delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check all books in the database
print(Book.objects.all())
