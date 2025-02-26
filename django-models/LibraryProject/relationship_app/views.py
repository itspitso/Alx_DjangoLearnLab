from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import View
from .models import Book
from .models import Library
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth import logout

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
