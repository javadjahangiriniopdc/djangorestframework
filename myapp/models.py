from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    family = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
