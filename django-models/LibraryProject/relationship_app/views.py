from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

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
