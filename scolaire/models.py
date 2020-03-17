from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1

# Create your models here.


class Individus(models.Model):
    guid = uuid1()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

