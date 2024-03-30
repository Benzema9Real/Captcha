from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    name = models.CharField('Название',max_length=50)
    author = models.CharField('Автор',max_length=50)
    title = models.TextField('Описание')
    date = models.IntegerField('Дата публикации')
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title






