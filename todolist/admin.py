from django.contrib import admin
from todolist.models import TodoItem, Collection, Collection_item

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Collection)
admin.site.register(Collection_item)

