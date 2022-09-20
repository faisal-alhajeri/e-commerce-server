from django.db.models import Q

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend, ModelBackend

MyUser = get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request,email=None, password=None, **kwargs):
        try:
            print(email)
           # Try to fetch the user by searching the username or email field
            user = MyUser.objects.get(Q(username=email)|Q(email=email))
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:

            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            MyUser().set_password(password)