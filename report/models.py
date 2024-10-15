from django.db import models
from django.contrib.auth.models import User

class Cuestionario(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    tipo_pregunta = models.CharField(max_length=10, default='checkbox')

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.BooleanField(default=False)

    def __str__(self):
        return f"Respuesta de {self.user.username} a {self.pregunta.texto}"

class Parroquia(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=255)
    parroquias = models.ManyToManyField(Parroquia)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=255)
    municipio = models.ManyToManyField(Municipio)
    def __str__(self):
        return self.nombre

class User(models.Model):
    nombre = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    reporte = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte de {self.user.nombre} en {self.municipio.nombre}, {self.parroquia.nombre}"