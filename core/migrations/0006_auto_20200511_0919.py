# Generated by Django 3.0.3 on 2020-05-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200511_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]