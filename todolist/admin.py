from django.contrib import admin
from todolist.models import  Collection, Task

# Register your models here.

admin.site.register(Collection)
admin.site.register(Task)

