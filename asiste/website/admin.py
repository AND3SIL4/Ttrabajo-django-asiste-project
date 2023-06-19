from django.contrib import admin
from .models import Aprendiz, Programa, Instructor, Ficha

# Register your models here.
admin.site.register(Aprendiz)
admin.site.register(Programa)
admin.site.register(Instructor)
admin.site.register(Ficha)
