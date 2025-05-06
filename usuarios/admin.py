from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Estudiante

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Rol',{'fields':('rol',)}),)

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Estudiante)