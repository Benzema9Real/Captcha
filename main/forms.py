from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['slug']
class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2','captcha')