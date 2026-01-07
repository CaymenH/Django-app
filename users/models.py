from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Date_of_birth = models.DateField(null=True, blank=True)
    Address= models.CharField(max_length=255, blank=True)
    City_town = models.CharField(max_length=255, blank=True)
    Country = models.CharField(max_length=255, blank=True)
    image = models.ImageField(default='media/profile_pics/default.png',
    upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
