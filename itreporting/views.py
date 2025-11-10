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
# Get all reported issues
    issues = Issue.objects.all()
# Create a context dictionary to pass to the template
    context = {'issues': issues}
# Render the report.html template with the context
    return render(request, 'itreporting/report.html', context)

