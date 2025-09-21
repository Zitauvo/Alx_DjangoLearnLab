from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField(null=True, blank=True)  # Added field

    def __str__(self):
        return f"{self.title} by {self.author}"

