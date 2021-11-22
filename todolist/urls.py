from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
]