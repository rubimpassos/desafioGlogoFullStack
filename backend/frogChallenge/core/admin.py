from django.contrib import admin

from .models import Food, ImportedFile


admin.site.register(Food)
admin.site.register(ImportedFile)
