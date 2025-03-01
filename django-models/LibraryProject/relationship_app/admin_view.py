from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin) 
def Admin(request):
    return "Hello Admin"