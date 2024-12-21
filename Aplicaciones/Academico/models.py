from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas = models.IntegerField()
    def __str__(self):
        return self.nombre