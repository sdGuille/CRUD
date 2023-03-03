from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False,
                             verbose_name='Title')
    image = models.ImageField(upload_to='images/', null=True,
                              verbose_name="Image")
    description = models.TextField(verbose_name="Description", null=True)

    def __str__(self):
        return self.title