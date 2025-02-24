from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return(request, "relationship_app/list_books.html", context)

class LibraryDetail(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

