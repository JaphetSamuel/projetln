from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Eleve (models.Model):
    guid = uuid4()
    matricule = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    numero = models.CharField(max_length=12)
    niveau = models.CharField(max_length=30, blank=False, default="sixieme")

    def __str__(self):
        return self.user.username


class Professeur (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matiere = models.CharField(max_length=100)
    guid = uuid4()

    def __str__(self):
        return self.user.username

