from django.contrib import admin

# Register your models here.

from .models import apto, pessoa

admin.site.register(pessoa)
admin.site.register(apto)
