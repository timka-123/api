from django.db import models

# Create your models here.


class License(models.Model):
    login = models.CharField(max_length=50)
    token = models.CharField(max_length=250)
