from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Router for BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns
urlpatterns = [
    # Existing ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes registered with the router
    path('', include(router.urls)),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
