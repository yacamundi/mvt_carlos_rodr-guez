from django.db import models

class Familiares(models.Model):
    nombre  = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=20)
    vivo = models.BooleanField()