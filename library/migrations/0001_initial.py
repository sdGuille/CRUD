# Generated by Django 4.1.7 on 2023-03-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Image')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
        ),
    ]
