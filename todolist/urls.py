from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.todo_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('collections/<int:id>/', views.collections, name='single_collection'),
    path('deleteCollection/<int:id>/', views.deleteCollection, name='deleteCollection'),
    path('udpate_task/<int:id>/', views.udpate_task, name='udpate_task'),
    path('deleteTask/<int:id>/', views.deleteTask, name='deleteTask'),
    path('logout/', views.todo_logout, name='logout'),
    path('signup/', views.todo_signup, name='signup'),
]
