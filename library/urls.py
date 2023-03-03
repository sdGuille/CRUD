from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('books', views.books, name='books'),
    path('books/create', views.create, name="create"),
]
