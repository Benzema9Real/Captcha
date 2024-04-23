from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    date_of_birth = models.IntegerField('Описание')
    avatar = models.ImageField('Аватар',upload_to='images/')








