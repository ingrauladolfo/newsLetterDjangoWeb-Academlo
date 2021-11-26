from django.db import models
from datetime import datetime, date

# Create your models here.
from tags.models import Tag


class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.URLField(max_length=300)
    target = models.CharField(max_length=100)
    frequency = models.IntegerField()
    date = models.DateField(auto_now_add=False, auto_now=True,)
    category = models.ManyToManyField(Tag, related_name="Newsletters")


    def __str__(self):
        return self.name

