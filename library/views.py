from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Book
from .forms import FormBook
# Create your views here


def home(request):
    return render(request, "pages/home.html")


def about_us(request):
    return render(request, 'pages/about_us.html')


def books(request):
    my_books = Book.objects.all()
    return render(request, 'books/index.html', {'my_books': my_books})


def create(request):
    form = FormBook(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form': form})


def update(request, id):
    book = Book.objects.get(id=id)
    form = FormBook(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, 'books/update.html', {"form": form})


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')
