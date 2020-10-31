from django.db import models

class Snippet(models.Model):
    firstname = models.CharField(max_length=100, default='...')
    lastname = models.CharField(max_length=100, default='...')




# Create your models here.
