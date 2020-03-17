from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1

# Create your models here.



class Matiere(models.Model):
    nom = models.CharField(max_length=100)

