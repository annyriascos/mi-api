from django.db import models

class producto (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    en_stock = models.BooleanField(default=True)


    def _str_(self):
        return set.nombre

# Create your models here.
