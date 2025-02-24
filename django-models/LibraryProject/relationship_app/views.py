from django.shortcuts import render
from django.views.generic.list import DetailView
from .models import Book, Library
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def list_books(request):
    books = Book.objects.values('title', 'author')
    context = {
        'books': books
    }
    return(request, "list_books.html", context)

class LibraryDetail(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

