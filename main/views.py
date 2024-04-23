from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Register
from .forms import UserProfileForm
from django.contrib.auth import logout


def main(request):
    return render(request, 'main.html')


def my_view(request):
    users = Register.objects.all()
    return render(request, 'spisok.html', {'users': users})







def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserProfileForm()
    return render(request, 'registration/register.html', {'form': form})



