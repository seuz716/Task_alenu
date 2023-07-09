from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    url_imagen = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
