from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.todo_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.todo_logout, name='logout'),
]