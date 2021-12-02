import collections

from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    collection_name = models.TextField(null=True)

    def __str__(self):
        return self.collection_name


class Task(models.Model):
    task = models.TextField(null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task
