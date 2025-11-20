from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue

from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .models import Issues

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})
def about(request):
    return HttpResponse('<h1>Student IT Services About</h1>')
def contact(request):
    return HttpResponse('<h1>contact information</h1>')

def report(request):
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues,Reported'}
    return render(request, 'itreporting/report.html', daily_report)

class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 10 # Optional pagination

class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'

