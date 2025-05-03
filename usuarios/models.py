from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    ROLES = (
        ('administrador','Administrador'),
        ('profesor','Profesor'),
        ('estudiante','Estudiante'),
    )

    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')

    def __str__(self):
        return f"{self.username} - {self.rol}"

# Tablas para Estudiante, profesor, administrador