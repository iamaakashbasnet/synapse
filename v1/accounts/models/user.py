from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from PIL import Image
from v1.accounts.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email',
                              max_length=120, unique=True)
    username = models.CharField(
        verbose_name='Username', max_length=30, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=30)
    last_name = models.CharField(verbose_name='Last name', max_length=30)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)  # pylint: disable=E1101
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)  # pylint: disable=E1101

    def __str__(self) -> str:
        return f'{self.username}'
