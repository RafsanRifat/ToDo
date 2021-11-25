from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content



class Collection(models.Model):
    collection_name = models.TextField()

    def __str__(self):
        return self.collection_name


class Collection_item(models.Model):
    task = models.TextField()
    collection_name = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

