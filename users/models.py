from django.db import models
from newsletters.models import Newsletter
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=200)
    admin = models.BooleanField(null=True)
    Newsletter = models.ForeignKey(Newsletter,
                                   on_delete=models.CASCADE,
                                   null=False, blank=False)

    # la fecha de creaacion del tag es la misma del newsletter

    def __str__(self):
        return self.name