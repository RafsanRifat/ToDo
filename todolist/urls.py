from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.todo_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('collection_list/<int:pk>/', views.collection_list, name='collection_list'),
    path('logout/', views.todo_logout, name='logout'),
    path('signup/', views.todo_signup, name='signup'),
]
