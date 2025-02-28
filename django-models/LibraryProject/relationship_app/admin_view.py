from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    user = UserProfile
    if user.role == 'Admin':
        return 'Admin'

@user_passes_test(is_admin) 
def Admin(request):
    return "Hello Admin"