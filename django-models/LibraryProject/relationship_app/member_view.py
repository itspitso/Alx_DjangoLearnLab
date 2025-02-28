from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_member(user):
    user = UserProfile
    if user.role == 'Member':
        return 'Member'

@user_passes_test(is_member)
def Member(request): 
    return "Hello Member"
