from django.urls import path
from django.urls import include
from . import views 
from .views import list_books, LibraryDetailView, LoginView, LogoutView
from . import admin_view
from .import librarian_view
from . import member_view

urlpatterns = [
    path('books/', list_books, name="list_books"),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]