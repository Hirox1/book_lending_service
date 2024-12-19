from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, full_name, email, username, mobile, password=None):
        if not email:
            raise ValueError('Email is required.')
        if not username:
            raise ValueError('Username is required.')
        if not mobile:
            raise ValueError('Mobile number is required.')
        if not full_name:
            raise ValueError('Full name is required.')

        email = self.normalize_email(email)
        user = self.model(
            full_name=full_name,
            email=email,
            username=username,
            mobile=mobile
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, username, mobile, password=None):
        user = self.create_user(
            full_name=full_name,
            email=email,
            username=username,
            mobile=mobile,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User Model
class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length=20, help_text='+(995) 5** - *** - ***')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username', 'mobile']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.id}) {self.full_name} - {self.mobile} - {self.email}'

