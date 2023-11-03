from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_Admin = models.BooleanField(default=False)
    is_Customer = models.BooleanField(default=False)
    is_Employee = models.BooleanField(default=False)