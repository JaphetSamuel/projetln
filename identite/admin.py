from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'guid']

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'matiere', 'guid']