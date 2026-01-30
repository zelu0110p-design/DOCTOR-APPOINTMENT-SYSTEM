from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
""" django.contrib.auth import from get_user_model
"""
class EmailBackEnd(ModelBackend):
    """ EmailBackEnd is a class for authenticate
    """
    def authenticate(self, username=None, password=None, **kwargs):
        """ authenticate the user
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None