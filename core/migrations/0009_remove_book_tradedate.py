# Generated by Django 3.0.3 on 2020-05-11 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tradeDate',
        ),
    ]