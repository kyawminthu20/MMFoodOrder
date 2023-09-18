from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from authentication.managers import UserManager


# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):

    class UserType(models.TextChoices):
        CUSTOMER = 'customer','Customer'
        FOOD_COLLECTOR = 'food_collector', 'Food Collector'
        FOOD_VENDOR = 'food_vendor', 'Food Vendor'
        ADMIN = 'admin', 'Admin'

    username = models.CharField(max_length=36, unique=True)
    password = models.CharField(max_length=64)
    user_type = ArrayField(models.CharField(max_length=20, choices=UserType.choices), size=4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField()
    house_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

