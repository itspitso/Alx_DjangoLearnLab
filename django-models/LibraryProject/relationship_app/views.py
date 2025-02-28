from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import View
from .models import Book
from .models import Library
from .models import UserProfile
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return(request, "templates/relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "templates/relationship_app/library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def register(request):
    form = UserCreationForm()
    return render(request, 'templates/relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'templates/relationship_app/login.html'
    form = AuthenticationForm()

class LogoutView(LogoutView):
    template_name = 'templates/relationship_app/logout.html'

def is_admin(user):
    if user.role == 'Admin':
        return 'Admin'
    
def is_librarian(user):
    if user.role == 'Librarian':
        return "Librarian"
    
def is_member(user):
    if user.role == 'Member':
        return 'Member'

@user_passes_test(is_admin) 
def Admin(request):
    return "Hello Admin"

@user_passes_test(is_librarian)
def Librarian(request):
    return "Hello Librarian"

@user_passes_test(is_member)
def Member(request): 
    return "Hello Member"
