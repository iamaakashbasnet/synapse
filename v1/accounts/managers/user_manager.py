from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have an username')
        if not first_name and last_name:
            raise ValueError('User must have a first name and last name.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have an username.')
        if not first_name and last_name:
            raise ValueError('User must have an first name and last name')

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user.save()
        return user
