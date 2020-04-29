from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(blank=True,verbose_name="Nombre", max_length=100)
    apellido = models.CharField(blank=True,verbose_name="Apellido", max_length=100)
    email = models.EmailField(blank=True,verbose_name="Correo", max_length=100)
    edad = models.IntegerField(null=True, blank = True)
    

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Contacto'
        verbose_name_plural = 'name'
    
        