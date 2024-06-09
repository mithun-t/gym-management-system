from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', home, name='home'),
    path('', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]