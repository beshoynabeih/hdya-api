from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    email = models.EmailField(null=False, max_length=255, unique=True)
    first_name = models.CharField(max_length=10, null=False)
    last_name = models.CharField(max_length=10, null=False)
    mobile = models.CharField(max_length=13, null=True)
    avatar = models.ImageField(null=True, upload_to='static/user/images/')
    address = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=10, null=True, blank=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    def __str__(self):
        return self.first_name + ' ' + self.last_name
