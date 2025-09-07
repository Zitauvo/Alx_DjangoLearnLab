from django.contrib import admin
from .models import Book

# Customize how Book appears in the admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in list view
    list_filter = ('author', 'publication_year')            # filter sidebar
    search_fields = ('title', 'author')                     # search box

# Register the model + custom admin
admin.site.register(Book, BookAdmin)
