from django.urls import path
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('books/', list_books, name="list_books"),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register')
]