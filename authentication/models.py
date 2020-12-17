from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    email = models.EmailField(null=False, max_length=255, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='static/user/images/')
    # governorate = models.CharField(max_length=30, null=True, blank=True)
    # city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',
                       'first_name',
                       'last_name']

    def get_username(self):
        return self.email

    def __str__(self):
        return self.first_name + ' ' + self.last_name
