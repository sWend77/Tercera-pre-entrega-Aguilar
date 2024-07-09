from .models import Avatar

def avatar(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=request.user)
        except Avatar.DoesNotExist:
            avatar = None
    else:
        avatar = None
    return {'avatar': avatar}