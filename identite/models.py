from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Eleve (models.Model):
    guid = uuid4()
    matricule = models.CharField(max_length=30)
    etablissement = models.ForeignKey('Etablissement', on_delete=models.CASCADE, blank=False, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=10)
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


class Etablissement (models.Model):
    nom  = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    guid = uuid4()

    def __str__(self):
        return self.nom

class Administration(models.Model):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username