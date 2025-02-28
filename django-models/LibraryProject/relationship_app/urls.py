from django.urls import path
from . import views 
from .views import list_books, LibraryDetailView, LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name="list_books"),
    path('library/<str:name>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.Admin, name='admin_view'),
    path('librarian/', views.Librarian, name='librarian_view'),
    path('member/', views.Member, name='member_view'),
]