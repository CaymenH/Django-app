from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'contact'})

def module(request):
    return render(request, 'itreporting/module.html',   {'title' : 'Module'})


def report(request):
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues,Reported'}
    return render(request, 'itreporting/report.html', daily_report)


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
    
