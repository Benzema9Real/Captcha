from django.contrib.admin import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Register


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        extra_kwargs = {'password': {'write_only': True}}  # Убедитесь, что пароль




class UserProfileForm(UserCreationForm):
    user = UserForm()
    class Meta:
        model = Register
        fields = ('user','date_of_birth', 'avatar')
    def create(self, validated_data):
        user_data = validated_data.pop('user')
# Хеширование пароля перед сохранением
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Register.objects.create(user=user, **validated_data)
        return profile