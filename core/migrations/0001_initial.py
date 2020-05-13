# Generated by Django 3.0.3 on 2020-05-09 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='hellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('tradeType', models.CharField(choices=[('S', 'Sale'), ('T', 'Trade'), ('G', 'Giveaway')], max_length=1)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=1000)),
                ('tradeDate', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
