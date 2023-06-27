from django.contrib import admin
from .models import Question, Choice

# pour ajouter le modele à la page admin
admin.site.register(Question)
admin.site.register(Choice)
