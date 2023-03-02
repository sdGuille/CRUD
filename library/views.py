from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def home(request):
    return HttpResponse("<h1>Welcome to my CRUD application</h1>")


def about_us(request):
    return render(request, 'about_us.html')
