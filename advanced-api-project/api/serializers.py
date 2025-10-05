from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Book model
# Includes validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model
# Includes nested BookSerializer to show all related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    """
    The 'books' field represents a reverse relationship.
    It uses the related_name='books' defined in the Book model's ForeignKey.
    This allows each Author to list all their books directly.
    """
