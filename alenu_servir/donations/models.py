from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Donacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidad = models.CharField(max_length=100, default="privada")
    tipo_regimen = models.CharField(max_length=50, default="régimen simple")
    identificacion = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(999999999999999)], default=222222222)
    tipo_identificacion = models.CharField(max_length=100, default="Nit")
    ciudad = models.CharField(max_length=50, default="Pasto")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    proposito = models.CharField(max_length=100, default="Sostenimiento")
    fuente = models.CharField(max_length=100, default="propias")
    confirmado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    url_imagen = models.URLField(blank=True)
    descripcion = models.TextField(max_length=100, default="" ) 
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    url_imagen = models.URLField(blank=True)

    def __str__(self):
        return f"Donación de {self.usuario.username}"
