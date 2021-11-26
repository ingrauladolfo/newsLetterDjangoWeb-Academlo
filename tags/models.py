from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.name