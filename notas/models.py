from django.db import models
from cursos.models import Inscripcion
# Create your models here.
class Nota(models.Model):
    inscripcion = models.OneToOneField(Inscripcion, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=5,decimal_places=2)
    nota2 = models.DecimalField(max_digits=5,decimal_places=2)

    nota_final = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    aprobado = models.BooleanField(default=False)

    def calcular_promedio(self):
        return (self.nota1 + self.nota2) / 2
    
    def save(self,*args, **kwargs):
        self.nota_final = self.calcular_promedio()
        self.aprobado = self.nota_final >= 66
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.inscripcion.estudiante.username} - {self.inscripcion.curso.nombre}"

        
