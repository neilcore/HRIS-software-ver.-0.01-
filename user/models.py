from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import validate_email

# from hris.HR import models


# class UserStatus(models.Model):
#     status = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f'{self.status}'
class CustomUserManager(UserManager):

    def _get_email_(self, email: str):
        validate_email(email)
        return self.normalize_email(email)
    def _create_user(self, email: str, password: str, commit: bool, is_staff: bool = False, is_superuser: bool = False):
        email = self._get_email_(email)
        user = User(email=email, password=password, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)

        if commit:
            user.save()
        return user
    def create_superuser(self, email: str, password: str, commit: bool = True):
        return self._create_user(email, password, is_staff=True, is_superuser=True, commot=commit)

    def create_user(self, email: str, password: str, commit: bool = True):
        return self._create_user(email, password, commit)


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

