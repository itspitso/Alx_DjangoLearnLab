from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_librarian(user):
    return user.userprofile.role == 'Librarian'
    
@user_passes_test(is_librarian)
def Librarian(request):
    return "Hello Librarian"