from django.urls import path
from .views import list_books, LibraryDetail

urlpatterns = [
    path('books/', list_books, name="list_books"),
    path('library/<str:name>/', LibraryDetail.as_view(), name='library_detail'),
]