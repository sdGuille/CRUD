from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def home(request):
    return render(request, "pages/home.html")


def about_us(request):
    return render(request, 'pages/about_us.html')


def books(request):
    return render(request, 'books/index.html')

