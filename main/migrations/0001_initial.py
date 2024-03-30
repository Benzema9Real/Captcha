# Generated by Django 5.0.3 on 2024-03-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('title', models.TextField(verbose_name='Описание')),
                ('date', models.IntegerField(verbose_name='Дата публикации')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]