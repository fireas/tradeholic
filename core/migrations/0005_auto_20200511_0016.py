# Generated by Django 3.0.3 on 2020-05-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_book_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='hellow',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('1', 'Genre 1'), ('2', 'Genre 2'), ('3', 'Genre 3'), ('4', 'Genre 4'), ('5', 'Genre 5'), ('6', 'Genre 6'), ('7', 'Genre 7'), ('8', 'Genre 8'), ('9', 'Genre 9')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
