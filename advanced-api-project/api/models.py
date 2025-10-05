from django.db import models

# The Author model stores information about book authors.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# The Book model stores book details.
# Each book is linked to one Author via a ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
