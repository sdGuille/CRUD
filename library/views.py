from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book
# Create your views here


def home(request):
    return render(request, "pages/home.html")


def about_us(request):
    return render(request, 'pages/about_us.html')


def books(request):
    my_books = Book.objects.all()
    return render(request, 'books/index.html', {'my_books': my_books})


def create(request):
    return render(request, 'books/create.html')


def update(request):
    return render(request, 'books/update.html')