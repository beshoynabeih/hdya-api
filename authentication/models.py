from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator


class User(AbstractUser):
    email = models.EmailField(null=False, max_length=255, unique=True)
    first_name = models.CharField(max_length=50, null=False,
                                  validators=[
                                      MinLengthValidator(limit_value=3),
                                      MaxLengthValidator(limit_value=50)
                                  ])
    last_name = models.CharField(max_length=50, null=False,
                                 validators=[
                                     MinLengthValidator(limit_value=3),
                                     MaxLengthValidator(limit_value=50)
                                 ])
    mobile = models.CharField(max_length=12,
                              null=True,
                              blank=True,
                              validators=[
                                  MinLengthValidator(limit_value=11),
                                  MaxLengthValidator(limit_value=12),
                                  RegexValidator(regex=r'^01(0|1|2|5)[0-9]{8}$',
                                                 message='only egypt mobile number  0100000000 or +20100000000')
                              ])
    avatar = models.ImageField(null=True, blank=True, upload_to='static/user/images/')
    # governorate = models.CharField(max_length=30, null=True, blank=True)
    # city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True,
                               validators=[
                                   MinLengthValidator(limit_value=3),
                                   MaxLengthValidator(limit_value=200)
                               ])
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',
                       'first_name',
                       'last_name',
                       'address',
                       'mobile',
                       'avatar',
                       'birth_date')

    def get_username(self):
        return self.email

    def __str__(self):
        return str(self.id)
