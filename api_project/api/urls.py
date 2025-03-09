# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    # Include the router URLs for BookViewSet
    path('', include(router.urls)),
]
