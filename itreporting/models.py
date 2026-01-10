from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Issue(models.Model):
    type = models.CharField(max_length=100, choices = [('Hardware','Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default = False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name = 'issues',
    on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.type} Issue in {self.room}'
    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs =
        {'pk': self.pk})
    

class Module(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    credit = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    availability = models.CharField (max_length=100, choices= [('Available', 'Available' ), ('Unavailable','Unavailable')])
    course = models.CharField(max_length= 50)
    def __str__(self):
        return f'{self.code} - {self.name}'


class Registration(models.Model):
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'module']
    
    def __str__(self):
        return f'Registration #{self.id}'