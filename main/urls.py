from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path

urlpatterns = [path('', views.main, name='main'),
               path('list/', views.my_view, name="list-book"),
               path('create_form', views.create, name='create_form'),
               path('register', views.register, name='register'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('<slug:slug>/', views.MyDetailView.as_view(), name='mydetail')
               ]
