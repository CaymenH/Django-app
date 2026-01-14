from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,  StudentUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Student

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            Student.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!') 
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})

@login_required
def profile(request):
    student_profile = request.user.student
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        s_form= StudentUpdateForm(request.POST, request.FILES,
        instance= student_profile)
        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        s_form = StudentUpdateForm(instance = student_profile)
    context = {'u_form': u_form, 's_form': s_form, 'title': 'Student Profile'}
    return render(request, 'users/profile.html', context)

