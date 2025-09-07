from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book, Library, UserProfile
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Role check helpers
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


# ----------------------------
# Role-Based Views
# ----------------------------
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# ----------------------------
# Book CRUD Views with Permissions
# ----------------------------
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        library_id = request.POST.get('library')
        if title and author_id and library_id:
            from .models import Author
            author = get_object_or_404(Author, id=author_id)
            library = get_object_or_404(Library, id=library_id)
            Book.objects.create(title=title, author=author, library=library)
            messages.success(request, 'Book added successfully!')
            return redirect('list_books')
    from .models import Author, Library
    authors = Author.objects.all()
    libraries = Library.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors, 'libraries': libraries})

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        library_id = request.POST.get('library')
        from .models import Author, Library
        book.author = get_object_or_404(Author, id=author_id)
        book.library = get_object_or_404(Library, id=library_id)
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('list_books')
    from .models import Author, Library
    authors = Author.objects.all()
    libraries = Library.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors, 'libraries': libraries})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
