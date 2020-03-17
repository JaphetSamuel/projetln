from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    pass