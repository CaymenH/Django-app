from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue


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

