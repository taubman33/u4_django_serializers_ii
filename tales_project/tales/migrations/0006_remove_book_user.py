# Generated by Django 4.0.4 on 2022-05-06 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0005_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]