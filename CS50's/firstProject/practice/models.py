from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Task(models.Model):
    Title= models.CharField(max_length=50)

    def __str__(self):
        return self.Title