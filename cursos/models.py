from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    profesor = models.ForeignKey(Usuario,on_delete=models.CASCADE, limit_choices_to={'rol':'profesor'},related_name='cursos_dictados')

    def __str__(self):
        return f"{self.nombre} - Inicia: {self.fecha_inicio}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Usuario,on_delete=models.CASCADE, limit_choices_to={'rol':'estudiante'},related_name='inscrito')

    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante','curso')

    def __str__(self):
        return f"{self.estudiante.username} Inscrito en: {self.curso.nombre}"

