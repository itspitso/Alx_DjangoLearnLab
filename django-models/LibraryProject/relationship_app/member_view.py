from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_member(user):
   return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def Member(request): 
    return "Hello Member"
