from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question) # Tellin that Question object has admin interface
admin.site.register(Choice)

