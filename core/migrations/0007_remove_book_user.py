# Generated by Django 3.0.3 on 2020-05-11 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200511_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]
