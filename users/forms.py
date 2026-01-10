from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', help_text='Your SHU email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=True)
        return user        


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        


class StudentUpdateForm(forms.ModelForm):
    class Meta:
     model =  Student
     fields = [ 'date_of_birth', 'address', 'city_town', 'country', 'image']
