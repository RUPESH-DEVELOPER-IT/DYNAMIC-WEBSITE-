from django.db import models

# Create your models here.

class tn(models.Model):
    name = models.CharField(max_length = 100)
    numbers=models.IntegerField(default=0)
