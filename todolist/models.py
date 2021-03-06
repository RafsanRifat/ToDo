import collections

from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    collection_name = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.collection_name


class Task(models.Model):
    task = models.CharField(null=True, max_length=500)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.task
