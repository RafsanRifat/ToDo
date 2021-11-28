import collections

from django.db import models


class Collection(models.Model):
    collection_name = models.TextField(null=True)

    def __str__(self):
        return self.collection_name


class Task(models.Model):
    task = models.TextField(null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task
