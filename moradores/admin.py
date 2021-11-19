from django.contrib import admin

# Register your models here.

from .models import apto, pessoa, prestador

admin.site.register(pessoa)
admin.site.register(apto)
admin.site.register(prestador)
