from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Issue, Module, Registration, Course
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import Student
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'contact'})

def module(request):
    module = {'modules': Module.objects.all(), 'title': 'Module'}
    return render(request, 'itreporting/module.html', module)


def report(request):
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues,Reported'}
    return render(request, 'itreporting/report.html', daily_report)

@login_required
def registration(request):
    student = get_object_or_404(Student, user=request.user)
    registrations =  Registration.objects.filter(student=student)
    context = {'registrations':registrations}
    return render(request, 'itreporting/registration.html', context)

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)  
    modules = course.modules.all()       
    context = {'course': course,'modules': modules,'title': course.name}
    return render(request, 'itreporting/course_detail.html', context)



def module_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    registrations = Registration.objects.filter(module=module)
    context = {'module': module,'registrations': registrations, 'title': module.name}
    return render(request, 'itreporting/module_detail.html', context)



class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination


class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue  # lowercase 'model'
    template_name = 'itreporting/issue_confirm_delete.html'
    success_url = reverse_lazy('itreporting:report')

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author
    

    
