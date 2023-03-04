from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name="home"),
    path('about_us', views.about_us, name="about_us"),
    path('books', views.books, name='books'),
    path('books/create', views.create, name="create"),
    path('books/update', views.update, name="update"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
