from django.urls import path
from . import views 
from django.core.mail import send_mail


urlpatterns = [
    path('', views.loginPage, name='loginForm'),
    path('create/', views.createPage, name='createForm'),
]