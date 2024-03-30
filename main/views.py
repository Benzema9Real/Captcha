from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book
from .forms import BookForm, RegisterForm
from django.contrib.auth import logout


def main(request):
    return render(request, 'main.html')


def my_view(request):
    users = Book.objects.all()
    return render(request, 'spisok.html', {'users': users})


class MyDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'
    slug_field = 'slug'


@login_required
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-book')
    else:
        form = BookForm()
    return render(request, 'add.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})



